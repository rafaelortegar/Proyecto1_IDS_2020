import os, sys
sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df


def load_ingestion(path):
    return load_df(path)


def date_transformation(col, df):
    pass


def numeric_transformation(col, df):
    pass


def categoric_transformation(col, df):
    pass


def cyclic_transformation(col, df):
    pass


def save_transformation(df, path):
    save_df(df, path)


def transform(path):
    df = load_ingestion(path)

    # transformaciones van aquí

    save_transformation(df, path)

