import pandas as pd

from sklearn.model_selection import train_test_split

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import save_df


def ingest_file(path):
    """Reads data from a csv located at path and returns a dataframe

    Parameters:
        path (string): Path where the csv file resides

    Returns:
        dataframe
    """
    df = pd.read_csv(path)

    return df


def generate_label(df):
    """Generates in the passed data frame a variable called `label`
    which is equal to 1 when `codigo_cierre` is (F) or (N) and 0
    in any other case

    Parameters:
        df (dataframe)
    """
    df['label'] = df['codigo_cierre'].str.split(' ', n=1, expand=False)
    df['label'] = df['label'].apply(lambda x: x[0][1])
    df['label'] = df['label'].apply(lambda x: 1 if x == 'F' or x == 'N' else 0)

    return df


def drop_cols(df):
    """Drops unused columns from passed dataframe. The variables that are eliminated are:
        - codigo_cierre
        - fecha_cierre
        - año_cierre
        - mes_cierre
        - hora_cierre
        - latitud
        - longitud
        - clas_con_f_alarma
        - delegacion_cierre
        - geopoint

    Parameters:
        df (dataframe)
    """
    dropped_columns = ['codigo_cierre', 'fecha_cierre', 'año_cierre', 'mes_cierre', 'hora_cierre',
                       'latitud', 'longitud', 'clas_con_f_alarma', 'delegacion_cierre', 'geopoint']
    df.drop(dropped_columns, axis='columns', inplace=True)

    return df


def save_ingestion(df, path):
    save_df(df, path)


def ingest(input_path, output_path_train,output_path_test):
    df = ingest_file(input_path)
    df = generate_label(df)
    df = drop_cols(df)
    etiqueta = df['label']
    features = df.copy()
    features.drop(columns = 'label', inplace = True)
    X_train, X_test, y_train, y_test = train_test_split(etiqueta, features)

    train = y_train.copy()
    train['label'] = X_train

    test =y_test.copy()
    test['label'] = X_test

    save_ingestion(train, output_path_train)
    save_ingestion(test, output_path_test)
