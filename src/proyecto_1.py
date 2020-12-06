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
model_output_df = '../output/model_results.pkl'
precision_recall_at_k_path = '../output/metricas/pr_at_k.pkl'
df_group_frecuencias_path = '../output/aequitas/df_group_frecuencias_path.pkl'
df_group_absolutas_path = '../output/aequitas/df_group_absolutas_path.pkl'
df_disparidad_limpio_path = '../output/aequitas/df_disparidad_limpio_path.pkl'
fairness_result_path = '../output/aequitas/fairness_result_path.pkl'
fairness_gaf_path = '../output/aequitas/fairness_gaf_path.pkl'
fairness_gof_path = '../output/aequitas/fairness_gof_path.pkl'



# constants
NO_AMBULANCIAS = 20

def main():
    ingest(csv_path,
           ingestion_pickle_path)

    transform(ingestion_pickle_path,
              transformation_pickle_path,
              test_df_pickle_path)

    feature_engineering(transformation_pickle_path,
                        feature_engineering_pickle_path,
                        test_df_pickle_path,
                        test_feature_engineering_pickle_path)

    # modeling(train_df_path=feature_engineering_pickle_path,
    #          test_df_path=test_feature_engineering_pickle_path,
    #          model_output_path=model_loop_path,
    #          n_units=NO_AMBULANCIAS,
    #          ingest_df_path=ingestion_pickle_path)

    model_evaluation(test_df_path = test_feature_engineering_pickle_path,
                     ingest_df_path = ingestion_pickle_path,
                     pr_at_k_path = precision_recall_at_k_path,
                     metrics_df_path = model_evaluation_path,
                     model_output_df_path = model_output_df)

    # bias_fairness(test_path = test_feature_engineering_pickle_path,
    #                 model_path = model_loop_path,
    #                 model_output_df_path = model_output_df,
    #                 df_group_frecuencias_path = df_group_frecuencias_path,
    #                 df_group_absolutas_path = df_group_absolutas_path,
    #                 df_disparidad_limpio_path = df_disparidad_limpio_path,
    #                 fairness_result_path = fairness_result_path,
    #                 fairness_gaf_path = fairness_gaf_path,
    #                 fairness_gof_path = fairness_gof_path)



if __name__ == '__main__':
    main()
