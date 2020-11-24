import os, sys
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df


def load_transformations(path):
    return load_df(path)


def generate_day_type(df):
    # 1 - indica un día con alto número de llamadas a C5
    # 0 - indica un día con bajo número de llamadas a C5
    # obtenidos de los datos históricos
    df['tipo_dia'] = df['dia_semana'].apply(lambda x: 1 if x == 'jueves' or x == 'viernes' or x == 'sabado' else 0)
    return df

def generate_trimestres(df):
    df['trimestre'] = np.ceil(df['mes'] / 3)
    df['trimestre'] = df['trimestre'].apply(lambda x: int(x))
    TRIMESTRES = 4
    df['sin_trim'] = np.sin(2 * np.pi * df.trimestre / TRIMESTRES)
    df['cos_trim'] = np.cos(2 * np.pi * df.trimestre / TRIMESTRES)
    df = df.astype({"trimestre":'category'})
    return df

def generate_llamada(df):
    search_string = "llamada"
    df['llamada'] = df['tipo_entrada'].apply(lambda x: 1 if search_string in x else 0)
    return df

def rename_incidente_c4(df):
    pass

def feature_generation(df):
    df = crea_timestamp(df)
    df = generate_day_type(df)
    df = generate_trimestres(df)
    df = generate_llamada(df)

    # one hot
    transformers = [('one_hot', OneHotEncoder(), ['delegacion_inicio'])]
    col_trans = ColumnTransformer(transformers, remainder="passthrough", n_jobs=-1, verbose=True)
    col_trans.fit(df)
    output_vars = col_trans.transform(df)
    final_df = pd.DataFrame(output_vars)


    return df


def feature_selection(df):
    pass


def save_fe(df, path):
    save_df(df, path)


def crea_timestamp(df):
    df['hora_creacion_copia'] = df['hora_creacion'].astype('str')
    df['fecha_creacion_copia'] = df['fecha_creacion'].astype('str')
    df['timestamp_creacion'] = df['fecha_creacion']+' '+df['hora_creacion']
    # convert the 'Date' column to datetime format
    df['timestamp_creacion']= pd.to_datetime(df['timestamp_creacion'])

    df.drop(columns = ['hora_creacion_copia','fecha_creacion_copia'], inplace = True)

    return df

def feature_engineering(input_path,output_path):
    df = load_transformations(input_path)
    df = feature_generation(df)
    df = feature_selection(df)
    save_df(df, output_path)
