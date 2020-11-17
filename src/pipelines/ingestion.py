from src.utils import save_df


def ingest_file(path):
    pass


def drop_cols(df):
    pass


def generate_label(df):
    df['label'] = df['codigo_cierre'].str.split(' ', n=1, expand=False)
    df['label'] = df['label'].apply(lambda x: x[0][1])
    df['label'] = df['label'].apply(lambda x: 1 if x == 'F' or x == 'N' else 0)


def save_ingestion(df):
    save_df(df, path)


def ingest(path):
    df = ingest_file(path)
    df = drop_cols(df)
    df = generate_label(df)
    save_ingestion(df, path)
