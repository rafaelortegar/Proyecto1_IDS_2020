sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df

def load_selected_model(path):
    load_df(path)

def group(df):
    pass

def bias(df):
    pass

def fairness(df):
    pass

def bias_fairness(path):
    model = load_selected_model(path)

    df = group(df)
    df = bias(df)
    df = fairness(df)
