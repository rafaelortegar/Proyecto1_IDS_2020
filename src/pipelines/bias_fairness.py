import pandas as pd
import matplotlib.pyplot as plt


from aequitas.group import Group
from aequitas.bias import Bias
from aequitas.fairness import Fairness
from aequitas.plotting import Plot


import os, sys
sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df




def load_selected_model(path):
    return load_df(path)

def group(df):
    g = Group()
    xtab, attrbs = g.get_crosstabs(df)
    absolute_metrics = g.list_absolute_metrics(xtab)
    df_frecuencias = xtab[[col for col in xtab.columns if col not in absolute_metrics]]
    df_absolutas = xtab[['attribute_name', 'attribute_value']+[col for col in xtab.columns if col in absolute_metrics]].round(2)

    aeq = Plot()

    FIG, AX = plt.subplots(figsize = (12,6))
    metric_for = aeq.plot_group_metric(xtab, 'for', ax=AX)
    FIG.savefig('../output/aequitas/group_FOR_plot.png')

    FIG, AX = plt.subplots(figsize = (12,6))
    metric_fnr = aeq.plot_group_metric(xtab, 'fnr', ax=AX)
    FIG.savefig('../output/aequitas/group_FNR_plot.png')

    FIG, AX = plt.subplots(figsize = (12,6))
    metric_npv = aeq.plot_group_metric(xtab, 'npv', ax=AX)
    FIG.savefig('../output/aequitas/group_NPV_plot.png')

    FIG, AX = plt.subplots(figsize = (12,6))
    metric_fpr = aeq.plot_group_metric(xtab, 'fpr', ax=AX)
    FIG.savefig('../output/aequitas/group_FPR_plot.png')

    FIG, AX = plt.subplots(figsize = (12,6))
    metric_prev = aeq.plot_group_metric(xtab, 'prev', ax=AX)
    FIG.savefig('../output/aequitas/group_PREV_plot.png')



    return df_frecuencias, df_absolutas, xtab, absolute_metrics

def bias(df, xtab):
    bias_object = Bias()
    bdf = bias_object.get_disparity_major_group(df=xtab, original_df=df, alpha=0.05)
    df_disparidad_sucio = bdf[['attribute_name', 'attribute_value'] + bias_object.list_disparities(bdf)].round(2)
    metrics = ['for_disparity', 'fnr_disparity', 'tnr_disparity', 'npv_disparity']
    df_disparidad_limpio = bdf[['attribute_name', 'attribute_value'] + metrics].round(2)

    #graficamos
    aeq = Plot()

    FIG, AX = plt.subplots(figsize = (10,10))
    for_disparity = aeq.plot_disparity(bdf,
                                   group_metric='for_disparity',
                                   attribute_name='delegacion',
                                   significance_alpha=0.05,
                                   fig=FIG, ax=AX)
    FIG.savefig('../output/aequitas/bias_FOR_DISPARITY_plot.png')

    FIG, AX = plt.subplots(figsize = (10,10))
    fnr_disparity = aeq.plot_disparity(bdf,
                                   group_metric='fnr_disparity',
                                   attribute_name='delegacion',
                                   significance_alpha=0.05,
                                   fig=FIG, ax=AX)
    FIG.savefig('../output/aequitas/bias_FNR_DISPARITY_plot.png')

    FIG, AX = plt.subplots(figsize = (10,10))
    tnr_disparity = aeq.plot_disparity(bdf,
                                   group_metric='tnr_disparity',
                                   attribute_name='delegacion',
                                   significance_alpha=0.05,
                                   fig=FIG, ax=AX)
    FIG.savefig('../output/aequitas/bias_TNR_DISPARITY_plot.png')

    FIG, AX = plt.subplots(figsize = (10,10))
    npv_disparity = aeq.plot_disparity(bdf,
                                   group_metric='npv_disparity',
                                   attribute_name='delegacion',
                                   significance_alpha=0.05,
                                   fig=FIG, ax=AX)
    FIG.savefig('../output/aequitas/bias_NPV_DISPARITY_plot.png')

    return df_disparidad_limpio, bdf, bias_object

def fairness(bdf, absolute_metrics, bias):
    fair = Fairness()
    fdf = fair.get_group_value_fairness(bdf)
    parity_determinations = fair.list_parities(fdf)
    fairness_result = fdf[['attribute_name', 'attribute_value']
        + absolute_metrics
        + bias.list_disparities(fdf)
        + parity_determinations].round(2)

    fairness_gaf = fair.get_group_attribute_fairness(fdf)

    fairness_gof = fair.get_overall_fairness(fdf)

    # graficamos
    aeq = Plot()

    FIG, AX = plt.subplots(figsize = (12,6))
    fairness_for = aeq.plot_fairness_group(fdf, group_metric='for', ax=AX);
    FIG.savefig('../output/aequitas/fairness_FOR_plot.png')

    FIG, AX = plt.subplots(figsize = (12,6))
    fairness_fnr = aeq.plot_fairness_group(fdf, group_metric='fnr', ax=AX);
    FIG.savefig('../output/aequitas/fairness_FNR_plot.png')

    FIG, AX = plt.subplots(figsize = (12,6))
    fairness_tnr = aeq.plot_fairness_group(fdf, group_metric='tnr', ax=AX);
    FIG.savefig('../output/aequitas/fairness_TNR_plot.png')

    FIG, AX = plt.subplots(figsize = (12,6))
    fairness_fdf = aeq.plot_fairness_group(fdf, group_metric='npv', ax=AX);
    FIG.savefig('../output/aequitas/fairness_NPV_plot.png')

    return (fairness_result,fairness_gaf,fairness_gof)

def bias_fairness(test_del_path, model_input_df_path,
                df_group_frecuencias_path, df_group_absolutas_path,
                df_disparidad_limpio_path, fairness_result_path,
                fairness_gaf_path, fairness_gof_path):

    model_output_df = load_df(model_input_df_path)

    y_scores = model_output_df['y_score']
    y_test = model_output_df['y_label']

    df = pd.DataFrame()
    df['score'] = y_scores
    df['label_value'] = y_test

    df_del = load_df(test_del_path)
    df['delegacion'] = list(df_del.delegacion_inicio)

    df_group_frecuencias, df_group_absolutas, xtab, absolute_metrics = group(df)
    df_disparidad_limpio, bdf, bias_object = bias(df, xtab)
    fairness_result, fairness_gaf,fairness_gof = fairness(bdf, absolute_metrics, bias_object)

    save_df(df_group_frecuencias, df_group_frecuencias_path)
    save_df(df_group_absolutas, df_group_absolutas_path)
    save_df(df_disparidad_limpio, df_disparidad_limpio_path)
    save_df(fairness_result, fairness_result_path)
    save_df(fairness_gaf, fairness_gaf_path)
    save_df(fairness_gof, fairness_gof_path)
