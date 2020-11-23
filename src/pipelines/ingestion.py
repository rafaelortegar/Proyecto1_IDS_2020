from src.utils import save_df
import pandas as pd


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


def drop_cols(df):
    """Drops unused columns from passed dataframe. The variables that are eliminated are:
        - codigo_cierre
        - fecha_cierre
        - año_cierre
        - mes_cierre
        - hora_cierre
        - clas_con_f_alarma
        - delegacion_cierre
        - geopoint

    Note: `folio` will be dropped until transformation.py file because it is needed to generate
    an important variable for our study.

    Parameters:
        df (dataframe)
    """
    dropped_columns = ['codigo_cierre', 'fecha_cierre', 'año_cierre', 'mes_cierre', 'hora_cierre', 'clas_con_f_alarma',
                       'delegacion_cierre', 'geopoint']
    df.drop(dropped_columns, axis='columns', inplace=True)


def save_ingestion(df, path):
    save_df(df, path)


def ingest(input_path, output_path):
    df = ingest_file(input_path)
    generate_label(df)
    drop_cols(df)
    save_ingestion(df, output_path)
