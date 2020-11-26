import os, sys
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df


def load_transformations(path):
    return load_df(path)

def crea_timestamp(df):
    df['hora_creacion_copia'] = df['hora_creacion']
    df['fecha_creacion_copia'] = df['fecha_creacion']
    df['hora_creacion_copia'] = df['hora_creacion_copia'].astype('str')
    df['fecha_creacion_copia'] = df['fecha_creacion_copia'].astype('str')
    df['timestamp_creacion'] = df['fecha_creacion_copia']+' '+df['hora_creacion_copia']
    # convert the 'Date' column to datetime format
    df['timestamp_creacion']= pd.to_datetime(df['timestamp_creacion'])

    df.drop(columns = ['hora_creacion_copia','fecha_creacion_copia'], inplace = True)

    return df

def generate_day_type(df):
    # 1 - indica un día con alto número de llamadas a C5
    # 0 - indica un día con bajo número de llamadas a C5
    # obtenidos de los datos históricos
    df['tipo_dia'] = df['dia_semana'].apply(lambda x: 1 if x == 'jueves' or x == 'viernes' or x == 'sabado' else 0)
    return df

def generate_trimestres(df):
    df['trimestre'] = np.ceil(df['mes'] / 3)
    df['trimestre'] = df['trimestre'].apply(lambda x: int(x))
    TRIMESTRES = 4
    df['sin_trim'] = np.sin(2 * np.pi * df.trimestre / TRIMESTRES)
    df['cos_trim'] = np.cos(2 * np.pi * df.trimestre / TRIMESTRES)
    df = df.astype({"trimestre":'category'})
    return df

def generate_llamada(df):
    search_string = "llamada"
    df['llamada'] = df['tipo_entrada'].apply(lambda x: 1 if search_string in x else 0)
    return df

def rename_incidente_c4(df):
    df.loc[df["incidente_c4"].str.contains('accidente-', case=False, na=None), "incidente_c4"] = 'accidente'
    df.loc[df["incidente_c4"].str.contains('cadaver-', case=False, na=None), "incidente_c4"] = 'cadaver'
    df.loc[df["incidente_c4"].str.contains('sismo-', case=False, na=None), "incidente_c4"] = 'sismo'
    df.loc[df["incidente_c4"].str.contains('mi ciudad-', case=False, na=None), "incidente_c4"] = 'mi ciudad'
    df.loc[df["incidente_c4"].str.contains('detencion ciudadana-', case=False, na=None), "incidente_c4"] = 'detencion ciudadana'
    df.loc[df["incidente_c4"].str.contains('lesionado-', case=False, na=None), "incidente_c4"] = 'lesionado'
    return df

def feature_generation(df):
    df = crea_timestamp(df)
    df = generate_day_type(df)
    df = generate_trimestres(df)
    df = generate_llamada(df)
    df = rename_incidente_c4(df)

    # one hot de delegación e incidente c4
    transformers = [('one_hot', OneHotEncoder(), ['delegacion_inicio','incidente_c4'])]
    col_trans = ColumnTransformer(transformers, remainder="passthrough", n_jobs=-1, verbose=True)
    col_trans.fit(df)
    output_vars = col_trans.transform(df)
    feature_names=col_trans.get_feature_names()
    final_df = pd.DataFrame(output_vars)
    final_df.columns = feature_names
    final_df.columns = final_df.columns.str.replace('one_hot__x0_', '')
    final_df.columns = final_df.columns.str.replace('one_hot__x1_', '')
    final_df.columns = final_df.columns.str.replace(' ', '_')
    final_df.columns = final_df.columns.str.replace('.', '')
    df = pd.DataFrame(final_df)

    return df


def feature_selection(df):
    print(df.columns)
    df = df.astype({"label":'category'})
    X = df.copy()
    y = X.label.values#.reshape(df.shape[0],)
    columnas_quitar = ['label','timestamp_creacion','fecha_creacion','hora_creacion','dia_semana','tipo_entrada']
    X.drop(columns = columnas_quitar,inplace = True)

    print('comienza modelado de feature selection:')
    # ocuparemos un RF
    classifier = RandomForestClassifier(oob_score=True, random_state=1234)

    # definicion de los hiperparametros que queremos probar
    # hyper_param_grid = {'n_estimators': [100, 500, 800, 1000],
    #                     'max_depth': [1, 5, 10, 20, 50],
    #                     'min_samples_split': [2, 5, 10]}
    hyper_param_grid = {'n_estimators': [100],
                    'max_depth': [2,5,10],
                    'min_samples_split': [2], 'max_features':[10]
                    }
    tscv = TimeSeriesSplit(max_train_size=None, n_splits=3)

    gs = GridSearchCV(classifier,
                           hyper_param_grid,
                           scoring = 'precision',
                           cv = tscv,
                           n_jobs = -1,return_train_score= True, verbose = True )

    gs.fit(X, y)

    datos_df_importancias = gs.best_estimator_.feature_importances_
    columnas_df_importancias = X.columns

    dataframe_importancias= pd.DataFrame(data = datos_df_importancias )

    dataframe_importancias['feature']=columnas_df_importancias
    dataframe_importancias.columns = ['importancia','feature']
    dataframe_importancias = dataframe_importancias.sort_values('importancia',ascending=False)
    dataframe_importancias =dataframe_importancias.loc[dataframe_importancias['importancia']>.069]
    lista_features_a_mantener = dataframe_importancias['feature']
    print('La lista de variables a mantener es:')
    print(lista_features_a_mantener)

    print('son en total:')
    print(len(lista_features_a_mantener))

    print('la respectiva importancia de cada feature al final fue:')
    print(dataframe_importancias)

    print('Los hiperparámetros del mejor modelo son:')
    print(gs.best_estimator_.get_params)

    df_importancias = dataframe_importancias.copy()
    lista_features = lista_features_a_mantener
    mejor_modelo = gs.best_estimator_

    return (df_importancias,lista_features,mejor_modelo)


def save_fe(df, path):
    save_df(df, path)



def feature_engineering(input_path,output_path):
    df = load_transformations(input_path)
    df = feature_generation(df)
    df_importancias,lista_features,mejor_modelo = feature_selection(df)

    df = df[lista_features]

    save_df(df, output_path)
