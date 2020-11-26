import os, sys
sys.path.insert(0, os.path.abspath(".."))

from src.pipelines.ingestion import ingest
from src.pipelines.transformation import transform
from src.pipelines.feature_engineering import feature_engineering


# paths
csv_path = '../data/incidentes-viales-c5.csv'
ingestion_train_pickle_path = '../output/ingest_df.pkl'
test_df_pickle_path = '../output/test_df.pkl'
transformation_pickle_path = '../output/transformation_df.pkl'
feature_engineering_pickle_path = '../output/fe_df.pkl'


def main():
    ingest(csv_path, ingestion_train_pickle_path)
    transform(ingestion_train_pickle_path, transformation_pickle_path,test_df_pickle_path)
    feature_engineering(transformation_pickle_path,feature_engineering_pickle_path)

if __name__ == '__main__':
    main()
