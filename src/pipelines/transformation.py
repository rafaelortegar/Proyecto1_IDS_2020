import os, sys
import pandas as pd
import numpy as np
import datetime

sys.path.insert(0, os.path.abspath(".."))
from src.utils.utils import load_df, save_df
from src.utils.clean import clean_df


def load_ingestion(path):
    return load_df(path)


def date_transformation(col, df):
    # arreglamos los strings de fechas
    # fix Dates
    # 31/02/19 --> 31/02/2019
    for ano in range(2013,2021):
        string_correccion_ano = str(ano)
        string_correccion_ano=string_correccion_ano[-2:]
        print(string_correccion_ano)

        for mes in range (1,13):
            if(mes<10):
                string_correccion_mes = '0'+str(mes)
            else:
                string_correccion_mes = str(mes)

            for dia in range(1, 32):
                elemento = dia

                if(elemento<10):
                    string_correccion = '0'+str(dia)+'/'+string_correccion_mes+'/'+string_correccion_ano
                    string_correcto = '0'+str(dia)+'/'+string_correccion_mes+'/20'+string_correccion_ano
                else:
                    string_correccion = str(dia)+'/'+string_correccion_mes+'/'+string_correccion_ano
                    string_correcto = str(dia)+'/'+string_correccion_mes+'/20'+string_correccion_ano

                #print(string_correccion)
                df.loc[df[col] == string_correccion, col] = string_correcto

    # Convertir columna en datetime
    df[col]=pd.to_datetime(df[col], format='%d/%m/%Y')

    return df

def fixing_hours(col, df):
    col_corregida = str(col)+'_corregida'

    # Arreglar Horas
    df_hrs_raras = df.loc[~df[col].str.contains(':', case=False, na=None)]
    hrs_raras = df_hrs_raras[col]
    hrs_raras = hrs_raras.astype('float')
    hours = [datetime.timedelta(days=float(num)) for num in hrs_raras]

    data_hr_corregida = {'folio':df_hrs_raras['folio'],col:df_hrs_raras[col],col_corregida:hours}
    dataframe_hrcorregida = pd.DataFrame(data=data_hr_corregida)
    dataframe_hrcorregida = df_hrs_raras.copy()
    dataframe_hrcorregida[col_corregida] = hours

    # Eliminamos microsegundos
    dataframe_hrcorregida[col_corregida]= dataframe_hrcorregida[col_corregida].dt.floor('s')
    #La pasamos a string para eliminar el texto de 0 días
    dataframe_hrcorregida[col_corregida] = dataframe_hrcorregida[col_corregida].astype(str)
    #Eliminamos el string de 0 dias
    dataframe_hrcorregida[col_corregida] = dataframe_hrcorregida[col_corregida].str.replace('0 days ', '')

    dataframe_hrcorregida[col] = dataframe_hrcorregida[col_corregida]
    df = df.append(dataframe_hrcorregida)
    df.drop_duplicates(keep='last',subset=['folio'],inplace = True)
    df.drop(['folio',col_corregida], axis='columns', inplace=True)
    return df


def generate_hora_decimal(df):
    df['hora_decimal'] = df['hora_creacion'].str.split(':', expand=False)
    df['hora_decimal'] = df['hora_decimal'].apply(lambda x: int(x[0]))# + int(x[1]) / 60 + int(x[2]) / 3600)
    return df

def generate_hora_ciclica(df):
    HOURS = 24
    df['sin_hr'] = np.sin(2 * np.pi * df.hora_decimal / HOURS)
    df['cos_hr'] = np.cos(2 * np.pi * df.hora_decimal / HOURS)
    df.drop(columns = 'hora_decimal', inplace = True)
    return df

def generate_mes_ciclico(df):
    MESES = 12
    df['sin_mes'] = np.sin(2 * np.pi * df.mes / MESES)
    df['cos_mes'] = np.cos(2 * np.pi * df.mes / MESES)
    return df

def integer_transformation(col, df):
    df = df.astype({col:'int64'})
    return df


def categoric_transformation(col, df):
    df = df.astype({col:'category'})
    return df


def cyclic_transformation(df):
    df = generate_hora_decimal(df)
    df = generate_hora_ciclica(df)

    # mes
    df = generate_mes_ciclico(df)

    return df

def impute_latitud(df):
    df = df[df.latitud.notna()]
    return df

def impute_longitud(df):
    df = df[df.longitud.notna()]
    return df

def impute_delegacion_inicio(df):
    # esta es para el train
    mode = df.delegacion_inicio.mode()[0]
    df['delegacion_inicio'].fillna(mode, inplace=True)
    return df, mode

def impute_with_value(df, col, value):
    # esta es para el test
    df[col].fillna(value, inplace=True)
    return df

def save_transformation(df, path):
    save_df(df, path)

def transform(input_path,output_path):
    df = load_ingestion(input_path)
    df = date_transformation('fecha_creacion',df)
    df = fixing_hours('hora_creacion',df)

    #integer_columns = ['mes']
    df = integer_transformation('mes',df)

    categoric_columns = ["dia_semana","delegacion_inicio", "incidente_c4" , "tipo_entrada"]

    for columna in categoric_columns:
        df = categoric_transformation(columna,df)

    #float_columns = []
    df = cyclic_transformation(df)

    df, mode_delegacion = impute_delegacion_inicio(df)

    df = clean_df(df)

    save_transformation(df, output_path)
