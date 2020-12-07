# Proyecto 1 y 2_IDS_2020
![](https://mcdatos.itam.mx/wp-content/uploads/2020/11/ITAM-LOGO.03.jpg)

Repositorio para el primer y segundo proyecto de la materia Introducción a Ciencia de Datos 2020

**Profesor:** M. Sc. Liliana Millán Núñez

**Integrantes del Equipo 9**

| # | Alumno                      | Clave única | Github        |
|:-:|:---------------------------:|:-----------:|:-------------:|
| 1 | Ángel Rafael Ortega Ramírez | 123972      | rafaelortegar |
| 2 | José Antonio Lechuga Rivera | 192610      | lechugaa      |
| 3 | Cecilia Avilés Robles       | 197817      | cecyar        |


## Objetivo

Predecir si una llamada al C5 para reportar un inicidente vial es **Falsa** o no. 

Para esto, contamos con los datos de accidentes viales en la CDMX reportados por C5 (Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano de la CDMX). En este conjunto se reporta: folio, fecha de creación del reporte, hora de creación del reporte, día de la semana de creación del reporte, fecha de cierre de reporte, hora de cierre de reporte, motivo del incidente dependiendo del tipo de emergencia, alcaldía donde sucedió el incidente, latitud y longitud del incidente, código de cierre del incidente reportado, clasificación del incidente, origen del incidente por tipo, alcaldía en que se dio resolución al incidente o emergencia. El diccionario completo de datos se encuentra en la siguiente [liga de dropbox](https://www.dropbox.com/sh/sj3q1y6gilv6yfv/AABZ7fhJc2xX2jNrGFWgOwu2a/Diccionario%20de%20Datos%20de%20Incidentes%20Viales.xlsx?dl=0).

Los registros que se reciben en el C5 se clasifican internamente por medio de un código de cierre:
- A = “Afirmativo”: Una unidad de atención a emergencias fue despachada, llegó al lugar de los hechos y confirmó la emergencia reportada
- N = “Negativo”: Una unidad de atención a emergencias fue despachada, llegó al lugar de los hechos, pero en el sitio del evento nadie confirmo la emergencia ni fue solicitado el apoyo de la unidad
- I = “Informativo”: Corresponde a solicitudes de información
- F = “Falso”: El incidente reportado inicialmente fue considerado como falso en el lugar de los hechos.
- D = “Duplicados”: El incidente reportado se registró en dos o más ocasiones procediendo a mantener un solo reporte como el original. Para el uso e interpretación correctos de la información, debe considerarse:

Para efectos de este proyecto, se clasificarán los registros antes mencionados de la siguiente manera:
- `1` cuando el código de cierre es `(F)` o `(N)`.
- `0` en otro caso.


## ¿Cómo reproducir los resultados de este repositorio?

Es importante comentar que las especificaciones del sistema operativo donde se creó este trabajo son:

- Nombre del SO: Ubuntu 20.04.1 LTS
- Tipo de SO: 64 bits
- Versión de Gnome: 3.36.3

Si usted desea reproducir los hallazgos encontrados en este trabajo, lo que tiene que hacer es lo siguiente:

1. Clonar el repositorio en su computadora en la dirección de su agrado con el comando: `git clone <url del repositorio> <nombre que desea poner al repositorio dentro de su sistema>`

2. Descargar el archivo `incidentes-viales-c5.csv` de [esta liga](https://www.dropbox.com/sh/sj3q1y6gilv6yfv/AABZ7wXdP6_NA0lqqpLB3bL9a/incidentes-viales-c5.csv?dl=0) y colocarlo en la carpeta `data`.

3. **Opcional, requiere pyenv:** Genera el ambiente virtual para este proyecto con el comando `pyenv virtualenv 3.7.4 nombre_de_tu_environment`

- Activa el ambiente virtual con el siguiente comando: `pyenv activate nombre_de_tu_environment`
  - Instalar ipykernel: `pip install ipykernel`
  - Hacer accesible el ambiente virtual al notebook de jupyter: `python -m ipykernel install --user --name nombre_de_tu_environment --display-name nombre_de_tu_environment`

4. Instalar el `requirements.txt` que se encuentra en el mismo directorio de este archivo `README.md` con el comando: `pip install -r requirements.txt`

5. Abra su terminal y desde ella entre al directorio raíz de este archivo. Dirígase después a la carpeta `/src`.

6. Ejecute el comando `python proyecto_1.py` y observe los resultados. 

- **Nota**: durante la ejecución del script se levantan varios warnings pero éstos no detienen la ejecución del mismo. Estos warnings se derivan ya que durante el entrenamiento del modelo existen algunas operaciones de división 0/0.


## ¿Qué archivos son importantes en este repositorio?

- En la carpeta `src`:
  - `proyecto_1.py`: script del Proyecto 1 y 2.
  - `/pipelines` y `/utils`: scripts utilizados por `proyecto_1.py`.
- En la carpeta `docs`:
  - `project_scoping.pdf`: Scoping del Proyecto.
  - `EDA_GEDA.html`: análisis exploratorio de los datos y sus gráficas correspondientes.
  - `SLIDE DECK_Priorización de ambulancias de respuesta a incidentes viales en la CDMX.pdf`: presentación preparada con los resultados del Proyecto 1.
  - `Reporte_proyecto_2.html`: reporte con resultados del Proyecto 2. 
- En la carpeta `notebooks`:
  - `EDA_GEDA.ipynb`: Jupyter Notebook con el que se hizo el análisis exploratorio de los datos y sus gráficas correspondientes.
  - `Reporte_proyecto_2.ipynb`: Jupyter Notebook con el que se hizo el reporte de resultados del Proyecto 2. 
- En la carpeta `output`:
  - `/metricas`: figuras guardadas de ROC curve, Precision, Recall y Tablas de métricas.
  - `/aequitas`: figuras guardadas con las gráficas de Aequitas.