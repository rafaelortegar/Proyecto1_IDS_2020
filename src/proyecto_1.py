import os, sys
sys.path.insert(0, os.path.abspath(".."))

from src.pipelines.ingestion import ingest
from src.pipelines.transformation import transform
from src.pipelines.feature_engineering import feature_engineering


# paths
csv_path = '../data/incidentes-viales-c5.csv'
ingestion_pickle_path = '../output/ingest_df.pkl'


def main():
    ingest(csv_path, ingestion_pickle_path)


if __name__ == '__main__':
    main()
