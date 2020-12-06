sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df

def load_model(path):
    load_df(path)

def metrics(models):
    pass

def save_metrics(df,path):
    save_df(df,path)

def model_evaluation(path):
    models = load_model(path)
    df = metrics(models)
    save_metrics(df,path)
