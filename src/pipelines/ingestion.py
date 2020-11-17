from src.utils import save_df


def ingest_file(path):
    pass


def drop_cols(df):
    pass


def generate_label():
    pass


def save_ingestion(df):
    save_df(df, path)


def ingest(path):
    df = ingest_file(path)
    df = drop_cols(df)
    df = generate_label(df)
    save_ingestion(df, path)
