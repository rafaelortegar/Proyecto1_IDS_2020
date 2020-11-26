# Proyecto 1 IDS Scoping

 1. **Nombre del proyecto:**
    Priorización de ambulancias de respuesta a incidentes viales en la CDMX<br/><br/>

 2. **Nombre de la organización:** 
    Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano de la CDMX (C5)<br/><br/>

 3. **Descripción del problema:**<br/><br/>

    3.1. ***¿Cuál es el problema al que se enfrenta?***
    En la Ciudad de México ocurren múltiples incidentes viales de forma diaria, sin embargo, solamente se cuenta con 20 ambulancias para atenderlos de forma simultánea. Estos eventos son detectados y reportados a través de múltiples canales, incluyendo por personas ajenas a las agencias gubernamentales. Por esta razón, muchos de los reportes (llamadas) resultan ser falsos provocando un uso ineficiente de las ambulacias de la CDMX y desatendiendo otros reportes de incidentes potencialmente verídicos.<br/><br/>
 
    3.2. ***¿Quién/qué es afectado por este problema?***
    Habitantes de la CDMX involucrados en un incidente vial que no reciben atención necesaria por falta de disponibilidad por parte de las ambulancias de gobierno.<br/><br/>

    3.3. ***¿Cuántas personas/organizaciones/lugares/etc. y qué tanto son afectados?***
    Con base en los datos (sin limpieza) reportados por C5 de [incidentes viales en la CDMX](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/table/?disjunctive.incidente_c4)
    entre 2014 y 2020, del total de incidentes viales reportados y/o detectados, alrededor de 600,000 de dichos reportes 
    constituyeron hechos reales que fueron atendidos por las ambulancias gubernamentales. No obstante, casi 300,000 de
    los reportes totales fueron falsos derivados de falsas alarmas y llamadas de broma, entre otros motivos. Estas cifras
    aproximadas implican que por cada 2 incidentes que requieren auxilio por parte de ambulancias en la CDMX, existe
    1 reporte falso de incidente que potencialmente desperdicia una ambulancia de atención, esto es aproximadamente el 5% de los recursos
    con los que cuenta la CDMX para atender este tipo de siniestros.<br/><br/>
    
    3.4. ***¿Por qué resolver este problema es una prioridad para la organización?***
    En el caso de incidentes viales, proporcionar una atención profesional, pero sobre todo oportuna, puede hacer la 
    diferencia entre la vida y la muerte de las personas involucradas o por lo menos, en el tipo de recuperación que
    experimentarán y la calidad de vida post-incidente. La C5 tiene por objeto captar información integral para la toma 
    de decisiones enfocadas en mejorar la calidad de vida de las y los capitalinos, por lo que atender oportunamente los
    reportes de incidentes, requiriendo un uso eficiente de las ambulancias, es una obligación tanto ética de todo 
    gobierno como laboral, dado el objetivo de creación de la C5.<br/><br/>
    
4. **Objetivos:** ¿Cuáles son las metas de negocio/política que serán logradas al resolver este problema y qué restricciones se tiene? (en orden de prioridad).<br/><br/>

   | # | Objetivo                                                                    | Restricciones                                                                        |
   |:-:|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
   | 1 | Mejorar la eficiencia de atención oportuna de los incidentes viales ocurridos en la CDMX  | Sólo se cuentan con 20 ambulancias para responder en caso de que un incidente ocurra |


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
   |**¿Qué es lo que contiene?** |Registro de los incidentes reportados y/o detectados por C5 a través de distintos medios. Los rubros incluidos son folio, hora de creación del reporte, fecha de creación del reporte, día de la semana de creación del reporte, fecha de cierre de reporte, hora de cierre de reporte, motivo del incidente, alcaldía donde sucedió el incidente, latitud y longitud del incidente, código de cierre del incidente reportado, clasificación del incidente, medio de reporte del incidente, alcaldía en que se dio resolución al incidente o emergencia. |
   |**¿Cuál es el nivel de granularidad?**|Nivel incidente|
   |**¿Con qué frecuencia es recolectado/ actualizado después de ser capturado?** |Mensual|
   |**Tiene identificadores confiables y únicos que pueden ser conectados a otras fuentes de datos?**|Sí, el folio del incidente|
   |**¿Quién es el propietario interno de los datos?**|Centro de Comando, Control, Cómputo, Comunicaciones y Contacto Ciudadano de la CDMX (C5)|
   |**¿Cómo se almacena?**|Base de datos de la CDMX|
   |**Comentarios adicionales**|Disponible [aquí](https://datos.cdmx.gob.mx/explore/dataset/incidentes-viales-c5/information/?disjunctive.incidente_c4&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibGF0aXR1ZCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiM2NmMyYTUifV0sInhBeGlzIjoibWVzZGVjaWVycmUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOm51bGwsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImluY2lkZW50ZXMtdmlhbGVzLWM1Iiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5pbmNpZGVudGVfYzQiOnRydWV9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)|
   <br/>

   B. *¿Qué datos se pueden obtener de fuentes externas, privadas o públicas?*<br/><br/>

   |   |Fuente 1| Fuente 2|
   |---|--------|---------|
   |**Nombre**|Registro Público Vehicular (REPUVE)| Registro de placas de la PGJ|
   |**¿Qué es lo que contiene?**|Descripción de vehículos a nivel república con los siguientes rubros: marca, modelo, año de modelo, clase, tipo, número de identificación vehicular, número de constancia de inscripción, placa, número de puertas, país de origen, versión, desplazamiento (cc/L), número de cilindros, número de ejes, planta de ensamble, datos complementarios, institución que lo inscribió, fecha de inscripción, hora de inscripción, entidad que emplacó, fecha de emplacado, fecha de última actualización, folio de constancia de inscripción, observaciones| Registro de placas de la CDMX con rubros de identificación y dirección de la persona física o moral a nombre del cual el vehículo está registrado|  
   |**¿Cuál es el nivel de granularidad?**|Vehículo| Vehículo
   |**¿Con qué frecuencia es recolectado/actualizado?**|N/A| N/A|
   |**Tiene identificadores confiables y únicos que pueden ser conectados a otras fuentes de datos?**|Sí, el número de identificación vehicular| Sí, las placas vehiculares |
   |**¿Quién es el propietario interno de los datos?**|Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública | Procuraduría General de Justicia de la CDMX|
   |**¿Cómo se almacena?**|Base de datos| Base de datos|
   |**Comentarios adicionales**|  |  |
   <br/>

   C. *En un mundo ideal, ¿qué datos adicionales te gustaría tener/recolectar que serían relevantes para el problema?*<br/>
   * Registro de números telefónicos de la Ciudad de México, buscando tener un historial por número telefónico de llamadas de broma.
   * Registro de antecedentes de infracciones de tránsito de los propietarios de los vehículos
   * Registro si el automóvil está asegurado y conocer su score de riesgo.
   * Transcripción de la conversación de la llamada telefónica de reporte
   <br/><br/>

7. **Análisis**<br/><br/>

   |  |Análisis 1:|
   |--|-----------|
   |Tipo de Análisis|Clasificación|
   |Propósito del análisis|Predecir si una llamada al C5 para reportar un inicidente vial es falsa o no|
   |¿Qué acción será informada por este análisis?|El envío de una ambulancia a la ubicación del incidente vial|
   |¿Cómo se validará el análisis utilizando datos existentes? <br/><br/>  ¿Qué metodología y métricas se utilizarán?|Empleando un set de prueba para evaluar el modelo de clasificación a partir de los datos históricos reportados por el C5. <br/><br/> Se utilizará la métrica de Precision, debido a que queremos atender los casos que estamos realmente seguros que lo necesitan.|
   <br/>

8. **Consideraciones éticas**<br/><br/>

   | Consideración | Descripción|
   |------|--------|
   |**Privacidad** <br/><br/> ¿Se trabaja con datos personales y/o sensibles que pueden ser individualmente indentificables? <br/><br/>Mencionarlos| A partir del set de datos reportados por C5 no, pero fácilmente el proyecto podría involucrar números de placas y por ende atribuir la propiedad del carro a una persona física o moral e inclusive determinar una dirección para el propietario.|
   |**Transparencia** <br/><br/> ¿Qué stakeholders deben estar informados sobre qué partes del proyecto?| Los operadores que asignan las ambulancias deberán estar informados sobre si la predicción indica que es una llamada verdadera, para enviar una ambulancia en ese momento. <br/><br/> |
   |**Discriminación/Equidad** <br/><br/> ¿Existen grupos específicos para quienes se busca asegurar equidad en los resultados?|En este aspecto no existen grupos éticos y minorías que se vean directamente afectados por dichas condiciones, pero es de suma importancia verificar que el modelo no se encuentre sesgado de ninguna manera (incluyendo aspectos geográficos) ya que esto implicaría por un lado un uso ineficiente de los recursos; pero por otra parte, y quizás más importante, negarle un servicio de salud a una porción de la población.<br/><br/> Se debe tener cuidado con los casos que el modelo interpreta como falsos, debido a que el modelo podría clasificar como falsas ciertas zonas con un alto historial de falsas alarmas.|
   |**Licencia Social** <br/><br/> Si toda la población del país se enterara del proyecto, ¿estarían de acuerdo con él? ¿Por qué?| Sí, porque forma parte del sentido común saber que la llegada oportuna de una ambulancia reduce significativamente el riesgo de repercusiones que afecten la calidad de vida a largo plazo o incluso significar la diferencia entre la vida y la muerte. Además también es conocido el problema que las llamadas de broma y falsas alarmas representan para la eficiencia de los servicios de emergencia de la CDMX.|
   |**Responsabilidad** <br/><br/> ¿Quiénes son las personas responsables por todo lo establecido anteriormente?|Consultores de ciencia de datos <br/><br/> Operadores de servicios de emergencia <br/><br/> Paramédicos de las ambulancias <br/><br/> C5 <br/><br/> Gobierno de la Ciudad de México|
   |**Otras consideraciones** como consentimiento, leyes, etc.|El C5 debe estar preparado para casos en los que un incidente que se clasificó como falso no sea atendido, en relación a política pública. <br/><br/> En caso de que todas las ambulancias estén asignadas y llega una llamada con un score más alto de ser verdadera, considerar enviar a la primer ambulancia en desocuparse o la que tenía el menor score de veracidad. **pensar solución**|
   <br/>

9. **¿Qué prueba de campo o prueba aleatorizada controlada puedes diseñar para validar el proyecto en el campo?**<br/><br/> Atender aleatoriamente llamadas clasificadas como falsas para seguir validando el modelo en tiempo real, así como dar un seguimiento a las métricas de precisión y valorar si los incidentes clasificados como verdaderos son efectivamente verídicos.<br/><br/> Para los casos clasificados como falsos, ver la posibilidad de enviar una patrulla para poder verificar la veracidad del incidente y poder recabar más datos para el modelo y la medición de su desempeño.<br/><br/>


10. **¿Quiénes son las organizaciones externas y los departamentos internos que deben estar involucrados?**<br/><br/>

   |Organización/Departamento|Descripción del involucramiento deseado|Nombre / Rol de Contraparte|
   |-------------------------|---------------------------------------|---------------------------|
   | El C5 | En todos los pasos del proyecto  | Tomadores de decisiones y proveedores del histórico de datos |
   | Los operadores telefónicos de emergencias | Creación de features | Dar algo de experiencia al modelo sobre identificación de llamadas falsas|
   | Gobierno de la CDMX | En todas las partes del proyecto | Facilitadores de información|
   | Secretaría de Comunicaciones y Transportes | En todas las partes del proyecto | Proveedor de recursos financieros e infraestructura |
   | Secretaría de Movilidad de la CDMX | En la parte inicial del proyecto | Fuente de datos|