import os, sys
sys.path.insert(0, os.path.abspath(".."))

from src.pipelines.ingestion import ingest
from src.pipelines.transformation import transform
from src.pipelines.feature_engineering import feature_engineering
from src.pipelines.modeling import modeling
from src.pipelines.model_evaluation import model_evaluation


# paths
csv_path = '../data/incidentes-viales-c5.csv'
ingestion_pickle_path = '../output/ingest_df.pkl'
test_df_pickle_path = '../output/test_df.pkl'
transformation_pickle_path = '../output/transformation_df.pkl'
feature_engineering_pickle_path = '../output/fe_df.pkl'
test_feature_engineering_pickle_path = '../output/test_fe_df.pkl'
model_loop_path = '../output/model_loop.pkl'
model_evaluation_path = '../output/metricas/metricas_offline.pkl'
precision_recall_at_k_path = '../output/metricas/model_loop.pkl'

# constants
NO_AMBULANCIAS = 20

def main():
    # ingest(csv_path,
    #        ingestion_train_pickle_path)
    #
    # transform(ingestion_pickle_path,
    #           transformation_pickle_path,
    #           test_df_pickle_path)

    # feature_engineering(transformation_pickle_path,
    #                     feature_engineering_pickle_path,
    #                     test_df_pickle_path,
    #                     test_feature_engineering_pickle_path)

    modeling(train_df_path=feature_engineering_pickle_path,
             test_df_path=test_feature_engineering_pickle_path,
             model_output_path=model_loop_path,
             n_units=NO_AMBULANCIAS,
             ingest_df_path=ingestion_pickle_path)

    model_evaluation(test_df_path = test_feature_engineering_pickle_path,
                     ingest_df_path = ingestion_pickle_path,
                     pr_at_k_path = precision_recall_at_k_path,
                     metrics_df_path = model_evaluation_path,
                     model_output_df_path = model_loop_path)



if __name__ == '__main__':
    main()
