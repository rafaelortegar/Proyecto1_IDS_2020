from src.pipelines.ingestion import ingest
from src.pipelines.transformation import transform
from src.pipelines.feature_engineering import feature_engineering


def main():
    path = ''
    ingest(path)
    transform(path)
    feature_engineering(path)
