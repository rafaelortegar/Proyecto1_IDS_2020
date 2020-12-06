import numpy as np
import pandas as pd
from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df

algorithms_dict = {
    'tree': 'tree_grid_search',
    'random_forest': 'rf_grid_search',
    'logistic_regression': 'logistic_regression_grid_search'
}

grid_search_dict = {
    'tree_grid_search': {
        'max_depth': [15, 20, 25],
        'min_samples_leaf': [3, 5, 7]
    },
    'rf_grid_search': {
        'n_estimators': [100, 300, 500],
        'max_depth': [5, 10, 15],
        'min_samples_leaf': [6, 8, 10]
    },
    'logistic_regression_grid_search': {
        'penalty': ['l1', 'l2', 'none']
    }
}

estimators_dict = {
    'tree': DecisionTreeClassifier(random_state=2004),
    'random_forest': RandomForestClassifier(oob_score=True, random_state=2222),
    'logistic_regression': LogisticRegression(random_state=1711)
}

def load_features(path):
    return load_df(path)


def magic_loop(algorithms, features, labels):
    best_estimators = []

    for algorithm in algorithms:
        estimator = estimators_dict[algorithm]
        grid_search_to_look = algorithms_dict[algorithm]
        grid_params = grid_search_dict[grid_search_to_look]

        tscv = TimeSeriesSplit(n_splits=5)
        gs = GridSearchCV(estimator, grid_params, scoring='average_precision',
                          return_train_score=True, cv=tscv, n_jobs=-1)

        # train
        gs.fit(features, labels)
        # best estimator
        best_estimators.append(gs)

    return best_estimators

def evaluate_precision(y_label, y_prob, cut):
    y_pred = [value >= cut for value in y_prob]
    precision = metrics.precision_score(y_label, y_pred)

    return precision


def max_precision(y_label, y_prob):
    best_precision = -1
    max_precision_cut = -1

    for i in range(1, 101):
        cut = i / 100
        precision = evaluate_precision(y_label, y_prob, cut)

        if precision > max_precision_cut:
            best_precision = precision
            max_precision_cut = cut

    return best_precision, max_precision_cut


def precision_at_k(y_labels, y_scores, k):
    threshold_index = int(len(y_scores) * k)

    # ordena de forma decremental
    ordered_y_scores = np.sort(y_scores)[::-1]
    threshold = ordered_y_scores[threshold_index]

    # generando labels de predicción
    y_predicted = np.array([score >= threshold for score in y_scores])

    return metrics.precision_score(y_labels, y_predicted)


def recall_at_k(y_labels, y_scores, k):
    threshold_index = int(len(y_scores) * k)

    # ordena de forma decremental
    ordered_y_scores = np.sort(y_scores)[::-1]
    threshold = ordered_y_scores[threshold_index]

    # generando labels de predicción
    y_predicted = np.array([score >= threshold for score in y_scores])

    return metrics.recall_score(y_labels, y_predicted)


def model_selection_by_precision_at_k(models, x_test, y_label, k):
    best_estimator = None
    best_precision = -1
    for model in models:
        estimator = model.best_estimator_
        y_score = estimator.predict_proba(x_test)[:, 1]
        precision = precision_at_k(y_label, y_score, k)

        if precision > best_precision:
            best_estimator = estimator
            best_precision = precision

    return best_estimator, best_precision


def save_models(model, output_path):
    save_df(model, output_path)


def modeling(train_df_path, test_df_path, model_output_path, n_units, ingest_df_path):

    # obteniendo dataset de entrenamiento
    df = load_features(train_df_path)
    df = df.astype({'label': 'category'})

    x_train = df.drop(columns=['label'])
    y_train = df.label

    # magic loop para obtener mejores modelos
    # algorithms = ['tree','random_forest', 'logistic_regression']
    algorithms = ['random_forest']
    best_models = magic_loop(algorithms, x_train, y_train)

    # obteniendo dataset de prueba
    df_test = load_df(test_df_path)
    df_test = df_test.astype({'label': 'category'})
    x_test = df_test[x_train.columns]
    y_test = df_test.label

    # obteniendo punto de corte dado el número de ambulancias
    df_ingest = load_df(ingest_df_path)
    k100 = df_ingest.label.value_counts()[0] / len(df_ingest.fecha_creacion.unique())
    k_n_units = n_units / k100

    print(f'Porcentaje de k para {n_units} ambulancias: {round(k_n_units, 2)}')

    model, precision = model_selection_by_precision_at_k(best_models, x_test, y_test, k_n_units)
    print(f"El mejor modelo es: {model}")
    print(f"Tiene una precisión en k-{round(k_n_units, 2)} de {precision}")

    save_models(model, model_output_path)
