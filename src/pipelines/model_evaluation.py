from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
import os, sys

sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df
from src.pipelines.modeling import precision_at_k, recall_at_k

def load_model(path):
    return load_df(path)

def generate_roc(y_test, y_scores, predicted_labels):
    print("Generando curva roc...")
    fpr, tpr, thresholds = roc_curve(y_test, y_scores)

    plt.figure(figsize=(12, 8))
    plt.clf()
    plt.plot([0, 1], [0, 1], 'k--', c="red")
    plt.plot(fpr, tpr)
    plt.title("ROC best RF, AUC: {}".format(round(roc_auc_score(y_test, predicted_labels), 3)))
    plt.xlabel("fpr")
    plt.ylabel("tpr")
    plt.savefig('../output/metricas/roc.png', dpi=300)


def pr_k_curve(y_labels, y_scores, k_target):
    k_values = list(np.arange(0.01, 1, 0.01))
    pr_k = pd.DataFrame()

    for k in k_values:
        d = dict()
        d['k'] = k
        d['precision'] = precision_at_k(y_labels, y_scores, k)
        d['recall'] = recall_at_k(y_labels, y_scores, k)

        pr_k = pr_k.append(d, ignore_index=True)

    # para la gráfica
    fig, ax1 = plt.subplots(figsize=(12, 8))
    ax1.plot(pr_k['k'], pr_k['precision'], label='precision')
    ax1.plot(pr_k['k'], pr_k['recall'], label='recall')

    # línea vertical
    plt.axvline(x=k_target, color='b', ls='--', label=f'k@{round(k_target, 2)}')
    plt.title('Curva precision-recall @k')
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0)

    plt.savefig('../output/metricas/precision-recall-curve.png', dpi=300)

    return pr_k


def get_metrics_report(y_test, y_scores):

    fpr, tpr, thresholds = roc_curve(y_test, y_scores)
    precision, recall, thresholds_2 = precision_recall_curve(y_test, y_scores)
    thresholds_2 = np.append(thresholds_2, 1)

    df_1 = pd.DataFrame({
        'threshold': thresholds_2,
        'precision': precision,
        'recall': recall})

    df_1['f1_score'] = 2 * (df_1.precision * df_1.recall) / (df_1.precision + df_1.recall)

    df_2 = pd.DataFrame({'tpr': tpr, 'fpr': fpr, 'threshold': thresholds})

    df_2['tnr'] = 1 - df_2['fpr']
    df_2['fnr'] = 1 - df_2['tpr']

    df = df_1.merge(df_2, on="threshold")

    return df


def model_metrics(y_test, y_scores, predicted_labels, k_target):
    generate_roc(y_test, y_scores, predicted_labels)
    pr_at_k_df = pr_k_curve(y_test, y_scores, k_target)
    metrics_df = get_metrics_report(y_test, y_scores)

    return pr_at_k_df, metrics_df


def cut_at_k(y_scores, k):
    threshold_index = int(len(y_scores) * k)

    # ordena de forma decremental
    ordered_y_scores = np.sort(y_scores)[::-1]
    return ordered_y_scores[threshold_index]


def model_evaluation(test_df_path, ingest_df_path, pr_at_k_path, metrics_df_path, model_input_path, model_output_df_path, n_units):

    # obteniendo dataset de prueba
    df_test = load_df(test_df_path)
    df_test = df_test.astype({'label': 'category'})
    features = ['accidente', 'cadaver', 'detencion_ciudadana', 'lesionado', 'sismo', 'llamada', 'tipo_dia',
                'sin_hr', 'cos_hr', 'sin_mes', 'cos_mes']
    x_test = df_test[features]
    y_test = df_test.label

    # recuperando modelo
    model = load_model(model_input_path)

    # obteniendo scores
    y_scores = model.predict_proba(x_test)[:, 1]

    # obteniendo punto de corte dado el número de ambulancias
    df_ingest = load_df(ingest_df_path)
    k100 = df_ingest.label.value_counts()[0] / len(df_ingest.fecha_creacion.unique())
    k_n_units = n_units / k100
    cut = cut_at_k(y_scores, k_n_units)

    # predicted labels
    predicted_labels = np.array([1 if score >= cut else 0 for score in y_scores])

    # obtendiendo métricas
    pr_at_k_df, metrics_df = model_metrics(y_test, y_scores, predicted_labels, k_n_units)

    # generando df de output
    df = pd.DataFrame()
    df['y_label'] = y_test
    df['y_score'] = y_scores
    df['y_predicted_label'] = predicted_labels

    save_df(pr_at_k_df, pr_at_k_path)
    save_df(metrics_df, metrics_df_path)
    save_df(df, model_output_df_path)
