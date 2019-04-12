# Text-mining-applied-project

## Descripción

Las metodologías en minería de datos fueron introducidas para proveer una vista holistica para en el proceso
de busqueda de conocimiento, mediante la aplicación de estadistica y algoritmos de machine learning. Su objetivo es definir un flujo generico, comenzando con la determinación de preguntas relevantes, lo que lleva al procesamiento de los datos en bruto y a menudo no estructurados y en ultima instancia descubrir nuevo conocimiento mediante la implementación de modelos que utilizan estos datos como insumo.

El proceso de correr o utilizar el modelo mas apropiado una vez se tiene la información adecuada es una tarea fácil, mientras que la adquisición, la limpieza y preparación de datos requiere un esfuerzo considerable de tiempo, ademas de ser éste el proceso responsable del exito o fracaso en la aproximación del modelo y su eficiencia.

Esta primera fase del proyecto contempla las tres fases iniciales del proceso CRISP-DM, el cual es un framework que permite traducir problemas del negocio en tareas de mineria de datos. A continuación se describen las herramientas, métodos y aprendizajes en cada fase implementada hasta el momento:

### Entendimiento de Negocio

Realizar un motor de búsqueda y una aplicación para poder navegar entre artículos similares. Ésta búsqueda debe ser sobre un conjunto de artículos que se encuentran almacenados en un sistema de archivos bajo Linux OS. La información utilizada para la construcción de estas aplicaciones son: los archivos en formato pdf y texto, y un archivo con la información de los meta datos de cada artículo.

### Entendimiento de los Datos

En esta fase fue importante entender la globalidad del problema, y tener discusiones a nivel técnico de alto nivel para empezar tener idea que cual sería la estructura mas adecuada para almacenar las palabras.

Se tuvieron inicialmente dos aproximaciones:

a) Una estructura de datos tipo diccionario [:palabra][:documento][:metricas]

b) Una estructura de datos tipo diccionario [:documento][:palabra][:documento]

Se selecciona la estructura b) la cual permite a nivel de documento tener las palabras correspondientes juntoc con sus métricas.

### Preparación de los Datos

Se realiza procesos de tokenizacion dada una expresión regular la cual permite limpiar el texto de palabras, que no tenga caracteres alfanumercos. 

Se utilizan metodos de stemming y lematización de palabras - de la libreria nltk - además de un diccionario de stopwords en idioma ingles.

Se construye un lector de propiedades de la metadata para incluirlas en el bag of words.

## Arquitectura del código 

## Guía de uso

Para correr el programa se necesita instalar las siguientes librerias

1. 

