import os, sys
sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df


def load_transformations(path):
    return load_df(path)


def feature_generation(df):
    df = crea_timestamp(df)
    return df


def feature_selection(df):
    pass


def save_fe(df, path):
    save_df(df, path)


def crea_timestamp(df):
    df['hora_creacion_copia'] = df['hora_creacion'].astype('str')
    df['fecha_creacion_copia'] = df['fecha_creacion'].astype('str')
    df['timestamp_creacion'] = df['fecha_creacion']+' '+df['hora_creacion']
    # convert the 'Date' column to datetime format
    df['timestamp_creacion']= pd.to_datetime(df['timestamp_creacion'])

    df.drop(columns = ['hora_creacion_copia','fecha_creacion_copia'], inplace = True)

    return df

def feature_engineering(path):
    df = load_transformations(path)
    df = feature_generation(df)
    df = feature_selection(df)
    save_df(df, path)
