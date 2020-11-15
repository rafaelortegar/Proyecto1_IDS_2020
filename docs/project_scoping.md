# Proyecto 1 IDS Scoping

 1. **Nombre del proyecto:**
    Priorización de ambulancias de respuesta a incidentes viales en la CDMX<br/><br/>

 2. **Nombre de la organización:** 
    Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano de la CDMX (C5)<br/><br/>

 3. **Descripción del problema:**<br/><br/>

    3.1. ***¿Cuál es el problema al que se enfrenta?***
    En la Ciudad de México ocurren múltiples incidentes viales de forma diaria, sin embargo, solamente se cuenta
    con 20 ambulacias para atender dichos incidentes de forma simultánea. Estos incidentes son detectados y reportados
    a través de múltiples canales incluso por personas ajenas a las agencias gubernamentales. Por esta disponibilidad, 
    muchos de los reportes (llamadas) resultan ser falsos provocando un uso ineficiente de las ambulacias de la CDMX y
    desatendiendo otros reportes de incidentes potencialmente verídicos.<br/><br/>
 
    3.2. ***¿Quién/qué es afectado por este problema?***
    Habitantes de la CDMX involucrados en un incidente vial que no reciben atención necesaria por falta de 
    disponibilidad por parte de las ambulancias de gobierno.<br/><br/>

    3.3. ***¿Cuántas personas/organizaciones/lugares/etc. y qué tanto son afectados?***
    Con base en los datos (sin limpieza) reportados por C5 de [incidentes viales en la CDMX](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/table/?disjunctive.incidente_c4)
    entre 2014 y 2020, del total de incidentes viales reportados y/o detectados, alrededor de 600,000 de dichos reportes 
    constituyeron hechos reales que fueron atendidos por las ambulancias gubernamentales. No obstante, casi 300,000 de
    los reportes totales fueron falsos derivados de falsas alarmas y llamadas de broma entre otros motivos. Estas cifras
    aproximadas implican que por cada 2 incidentes que requieren auxilio por parte de ambulancias en la CDMX, existe
    1 reporte falso de incidente que potencialmente desperdicia una ambulancia de atención, esto es el 5% de los recursos
    con los que cuenta la CDMX para atender este tipo de siniestros.<br/><br/>
    
    3.4. ***¿Por qué resolver este problema es una prioridad para la organización?***
    En el caso de incidentes viales, proporcionar una atención profesional, pero sobre todo oportuna, puede hacer la 
    diferencia entre la vida y la muerte de las personas involucradas o por lo menos, en el tipo de recuperación que
    experimentarán y la calidad de vida post-incidente. La C5 tiene por objeto captar información integral para la toma 
    de decisiones enfocadas en mejorar la calidad de vida de las y los capitalinos, por lo que atender oportunamente los
    reportes de incidentes, requiriendo un uso eficiente de las ambulancias, es una obligación tanto ética de todo 
    gobierno como laboral dado el objetivo de creación de la C5.<br/><br/>
    
4. **Objetivos:** Cuáles son las metas de negocio/política que serán logradas al resolver este problema y qué restricciones se tiene? (en orden de prioridad).<br/><br/>

   | # | Objetivo                                                                    | Restricciones                                                                        |
   |:-:|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
   | 1 | Mejorar la atención oportuna de los incidentes viales ocurridos en la CDMX  | Solo se cuentan con 20 ambulancias para responder en caso de que un incidente ocurra |


<br/>

5. **Acciones**<br/><br/>

   |                                                                 |Acción 1                                                                                       |
   |-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
   |**Acción:**                                                      |Enviar ambulancia al lugar del incidente en caso de que la llamada sea verdadera               |
   |**¿Quién está ejecutando la acción?**                            |Paramédicos asignados a las ambulancias de gobierno de la CDMX                                 |
   |**¿Sobre quién o qué se está ejecutando la acción?**             |Personas involucradas en un incidente vial                                                     |
   |**¿Con qué frecuencia hay que tomar la acción?**                 |Diaria, es reactiva desencadenada por una llamada de reporte al C5 que se clasifica como cierta|
   |**¿Qué canales se usan o se pueden usar para tomar esta acción?**|Se desencadena por un reporte al C5, pero la acción es realizada en persona por los paramédicos|
   <br/>

6. **Datos** <br/>

    A. *¿Qué fuentes de datos internas tenemos?*<br/><br/>

   |                         |Fuente 1                                                  |
   |-------------------------|----------------------------------------------------------|
   |**Nombre**                   |Incidentes viales reportados por C5|
   |**¿Qué es lo que contiene?** |Registro de los incidentes reportados y/o detectados por C5 a través de distintos medios. Los rubros que incluidos son folio, hora de creación del reporte, fecha de creación del reporte, día de la semana de creación del reporte, fecha de cierre de reporte, hora de cierre de reporte, motivo del incidente, alcaldía donde sucedió el incidente, latitud y longitud del incidente, código de cierre del incidente reportado, clasificación del incidente, medio de reporte del incidente, alcaldía en que se dio resolución al incidente o emergencia. |
   |**¿Cuál es el nivel de granularidad?**|Nivel incidente|
   |**¿Con qué frecuencia es recolectado/ actualizado después de ser capturado?** |Mensual|
   |**Tiene identificadores confiables y únicos que pueden ser conectados a otras fuentes de datos?**|Sí, el folio del incidente|
   |**¿Quién es el propietario interno de los datos?**|Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano de la CDMX|
   |**¿Cómo se almacena?**|Base de datos de la CDMX|
   |**Comentarios adicionales**|Disponible [aquí](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/information/?disjunctive.incidente_c4&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibGF0aXR1ZCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifV0sInhBeGlzIjoibWVzZGVjaWVycmUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOm51bGwsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImluY2lkZW50ZXMtdmlhbGVzLWM1Iiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5pbmNpZGVudGVfYzQiOnRydWV9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)|
   <br/>

   B. *¿Qué datos se pueden obtener de fuentes externas, privadas o públicas?*<br/><br/>

   |   |Fuente 1| Fuente 2|
   |---|--------|---------|
   |**Nombre**|Registro Público Vehicular (REPUVE)| Registro de placas de la PGJ|
   |**¿Qué es lo que contiene?**|Descripción de vehículos a nivel repúplica con los siguientes rubros: marca, modelo, año de modelo, clase, tipo, número de identificación vehicular, número de constancia de inscripción, placa, número de puertas, país de origen, version, desplazamiento (cc/L), número de cilindros, número de ejes, planta de ensamble, datos complementarios, institución que lo inscribió, fecha de inscripción, hora de inscripción, entidad que emplacó, fecha de emplacado, fecha de última actualización, folio de constancia de inscripción, observaciones| Registro de placas de la CDMX con rubros de identificación y dirección de la persona física o moral a nombre del cual el vehículo está registrado|  
   |**¿Cuál es el nivel de granularidad?**|Vehículo| Vehículo
   |**¿Con qué frecuencia es recolectado/actualizado?**|N/A| N/A|
   |**Tiene identificadores confiables y únicos que pueden ser conectados a otras fuentes de datos?**|Sí, el número de identificación vehicular| Sí, las placas vehiculares |
   |**¿Quién es el propietario interno de los datos?**|Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública | Procuraduría General de Justicia de la CDMX|
   |**¿Cómo se almacena?**|Base de datos| Base de datos|
   |**Comentarios adicionales**|  |  |
   <br/>

   C. *En un mundo ideal, ¿qué datos adicionales te gustaría tener/recolectar que serían relevantes para el problema?*<br/>
   * Registro de números telefónicos de la Ciudad de México
   * Registro de antecedentes de infracciones de tránsito de los propietarios de los vehículos
   <br/><br/>

7. **Análisis**<br/><br/>

   |  |Análisis 1:|
   |--|-----------|
   |Tipo de Análisis|Clasificación|
   |Propósito del análisis|Predecir si una llamada al C5 para reportar un inicidente vial es falsa o no|
   |¿Qué acción será informada por este análisis?|El envío de una ambulancia a la ubicación del incidente vial|
   |¿Cómo se validará el análisis utilizando datos existentes? <br/><br/>  ¿Qué metodología y métricas se utilizarán?|Empleando un set de validación del modelo de clasificación a partir de los datos históricos reportados por la C5|
   <br/>

8. **Consideraciones éticas**<br/><br/>


   | Consideración | Descripción|
   |------|--------|
   |**Privacidad** <br/><br/> ¿Se trabaja con datos personales y/o sensibles que pueden ser individualmente indentificables? <br/><br/>Mencionarlos||
   |**Transparencia** <br/><br/> ¿Qué stakeholders deben estar informados sobre qué partes del proyecto?||
   |**Discriminación/Equidad** <br/><br/> ¿Existen grupos específicos para quienes se busca asegurar equidad en los resultados?||
   |**Licencia Social** <br/><br/> Si toda la población del país se enterara del proyecto, ¿estarían de acuerdo con él? ¿Por qué?||
   |**Responsabilidad** <br/><br/> ¿Quiénes son las personas responsables por todo lo establecido anteriormente?||
   |**Otras consideraciones** como consentimiento, leyes, etc.||
   <br/>

9. **¿Qué prueba de campo o prueba aleatorizada controlada puedes diseñar para validar el proyecto en el campo?**<br/><br/>


10. **¿Quiénes son las organizaciones externas y los departamentos internos que deben estar involucrados?**<br/><br/>

|Organización/Departamento|Descripción del involucramiento deseado|Nombre / Rol de Contraparte|
|-------------------------|---------------------------------------|---------------------------|
||||

