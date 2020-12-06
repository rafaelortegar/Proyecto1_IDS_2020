import os, sys
sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df
from sklearn.tree import DecisionTreeClassifier

def load_features(path):
    return load_df(path)

def magic_loop(algorithms):
    pass

def save_models(models,path):
    save_df(models,path)

def modeling(path):
    df = load_features(path)
    algorithms = ['tree','random_forest']
    models = magic_loop(algorithms)
    save_models(models,path)
