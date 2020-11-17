from src.utils import load_df, save_df


def load_transformations(path):
    return load_df(path)


def feature_generation(df):
    pass


def feature_selection(df):
    pass


def save_fe(df, path):
    save_df(df, path)


def feature_engineering(path):
    df = load_transformations(path)
    df = feature_generation(df)
    df = feature_selection(df)
    save_df(df, path)
