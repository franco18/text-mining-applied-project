# Text-mining-applied-project

## Descripción

Las metodologías en minería de datos fueron introducidas para proveer una vista holística en el proceso
de búsqueda de conocimiento, mediante la aplicación de estadística y algoritmos de machine learning. Su objetivo es definir un flujo genérico, comenzando con la determinación de preguntas relevantes, lo que lleva al procesamiento de los datos en bruto y a menudo no estructurados y en última instancia descubrir nuevo conocimiento mediante la implementación de modelos que utilizan estos datos como insumo.

El proceso de correr o utilizar el modelo más apropiado una vez se tiene la información adecuada es una tarea fácil, mientras que la adquisición, la limpieza y preparación de datos requiere un esfuerzo considerable de tiempo, además de ser éste el proceso responsable del éxito o fracaso en la aproximación del modelo y su eficiencia.

Esta primera fase del proyecto contempla las tres fases iniciales del proceso CRISP-DM, el cual es un framework que permite traducir problemas del negocio en tareas de minería de datos. A continuación se describen las herramientas, métodos y aprendizajes en cada fase implementada hasta el momento:

### Entendimiento de Negocio

Realizar un motor de búsqueda y una aplicación para poder navegar entre artículos similares. Ésta búsqueda debe ser sobre un conjunto de artículos que se encuentran almacenados en un sistema de archivos bajo Linux OS. La información utilizada para la construcción de estas aplicaciones son: los archivos en formato pdf y texto, y un archivo con la información de los meta datos de cada artículo.

### Entendimiento de los Datos

En esta fase fue importante entender la globalidad del problema, y tener discusiones a nivel técnico de alto nivel para empezar tener idea que cual sería la estructura más adecuada para almacenar las palabras.

Se tuvieron inicialmente dos aproximaciones:

a)
```python
[:palabra][:documento][:propiedades]
```
b) 

```python
[:documento][:palabra][:propiedades]
```

Se selecciona la estructura b) la cual permite a nivel de documento tener las palabras correspondientes junto con sus métricas.

### Preparación de los Datos

Se realiza procesos de tokenización dada una expresión regular la cual permite limpiar el texto de palabras, que no tenga caracteres alfanuméricos.

Se utilizan métodos de stemming y lematización de palabras - de la librería nltk - además de un diccionario de stopwords en idioma inglés.

Se construye un lector de propiedades de la metadata para incluirlas en el bag of words [ver codigo](https://github.com/franco18/text-mining-applied-project/tree/master/xml_parser)

## Arquitectura del código

## Guía de uso

Para correr el programa se necesita instalar las siguientes librerías

1. Instalar las librerias 'stopwords','punkt', 'wordnet' de la siguiente manera:
```python
nltk.download(['stopwords','punkt', 'wordnet'])
```

2. Instalar librería xmltodict, para mas información ver documentación [aquí](https://github.com/martinblech/xmltodict#xmltodict)

3. Cada vez que se agregue un nuevo archivo se debe generar el bag of words. Para esto se ejecuta paso a paso el notebook llamado 

```python
ProyectoIntegrador.ipynb
```

4. En caso de necesitar generar de nuevo la información de la metadata, se debe ejecutar paso a paso el notebook llamado

```python
parser_metadata.ipynb
```

Ubicado en la siguiente [ruta](https://github.com/franco18/text-mining-applied-project/blob/master/xml_parser/parser_metadata.ipynb)

## Documentación detallada del proyecto

Para mas información del proyecto ingresa a la wiki dando click [aquí](https://github.com/franco18/text-mining-applied-project/wiki/Documentaci%C3%B3n-detallada-proyecto)

