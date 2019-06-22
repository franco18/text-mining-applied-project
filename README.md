
# Text-mining-applied-project

## Descripción

Las metodologías en minería de datos fueron introducidas para proveer una vista holística en el proceso
de búsqueda de conocimiento, mediante la aplicación de estadística y algoritmos de machine learning. Su objetivo es definir un flujo genérico, comenzando con la determinación de preguntas relevantes, lo que lleva al procesamiento de los datos en bruto y a menudo no estructurados y en última instancia descubrir nuevo conocimiento mediante la implementación de modelos que utilizan estos datos como insumo.

El proceso de correr o utilizar el modelo más apropiado una vez se tiene la información adecuada es una tarea fácil, mientras que la adquisición, la limpieza y preparación de datos requiere un esfuerzo considerable de tiempo, además de ser éste el proceso responsable del éxito o fracaso en la aproximación del modelo y su eficiencia.

Esta primera fase del proyecto contempla las cuatro fases iniciales del proceso CRISP-DM, el cual es un framework que permite traducir problemas del negocio en tareas de minería de datos. A continuación se describen las herramientas, métodos y aprendizajes en cada fase implementada hasta el momento:

### Entendimiento de Negocio

Realizar un motor de búsqueda y una aplicación para poder navegar entre artículos similares. Esta búsqueda debe ser sobre un conjunto de artículos que se encuentran almacenados en un sistema de archivos bajo Linux OS. La información utilizada para la construcción de estas aplicaciones son: los archivos en formato pdf y texto, y un archivo con la información de los meta datos de cada artículo.

### Entendimiento de los Datos

Son un conjunto de documentos o de datos no estructurados compuestos por palabras. Se cuenta con 980 documentos en diferentes formatos de texto como lo son: .txt, .pdf y .dc

Dichos documentos pertenecen al mismo dominio de interés, por ejemplo: ingeniería, medicina, o astronomía, entre muchos otros campos de conocimiento o aplicación.

En esta fase también fue necesario entender la globalidad del problema, y tener discusiones a nivel técnico de alto nivel para empezar tener idea de cual sería la estructura más adecuada para almacenar las palabras.

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

#### Nota

Luego de las sugerencias dadas en la presentación se realiza otra solución utilizando la librería sklearn.feature_extraction.text.CountVectorizer el cual permite generar el vocabulario y la matriz dispersa de frecuencia de pablaras por documento. Esta estructura facilitara la busqueda entre similitud de documentos, y aplicación de algoritmos de machine learning en general.

Para ver mas ingresar al notebook que se encuentra [aquí](https://github.com/franco18/text-mining-applied-project/blob/master/second_approach/BagOfWordsSecondApproach.ipynb) 


### Preparación de los Datos

A continuación, se describe la manera en que se lleva a cabo el proceso de pre procesamiento de los datos en una primeria instancia para luego pasar a la etapa de etapa de Búsqueda y Recuperación, dicho procedimiento aplica tanto para los datos globales así como para la búsqueda o Query.

La manera en que se almacenarán los datos es por medio de un diccionario, que es una estructura de datos que facilita su manipulación y tratamiento puesto que utiliza una clave para acceder a un valor. El proceso para preparar los datos consta de varias etapas:

1. Validar que sólo se trabaje con elementos alfanuméricos
2. Tokenización, que es segmentar el texto mediante espacios en blanco o signos de puntuación definidos
3. Stemming, que es convertir cada token a su propia forma de raíz utilizando reglas gramaticales definidas
4. Lematización, que es llevar los tokens a su forma canónica
5. Eliminación de stop-words, artículos, conjunciones y preposiciones
6. Verificar que las palabras restantes tengan una longitud mayor a 1

Luego de esto, se almacena en el diccionario que llamamos Bag of Words, junto con el conteo de la frecuencia de cada palabra asociada.

Adicional a lo antarior, se construye un lector de propiedades de la metadata para incluirlas en el bag of words [ver codigo](https://github.com/franco18/text-mining-applied-project/tree/master/xml_parser)

### Modelación


#### Primera Entrega
Dentro de los métodos para recuperar información de los textos, existen varios tipos de modelos. Por el momento, los modelos que están implementados para la recuperación de información son:

1. **Term Frequency (TF):** Es la técnica más simple para reconocer la relevancia de un término dentro de un texto. Básicamente realiza el conteo de la palabra en el texto y mientras más grande sea este número más relevante es
2. **Relative Term Frequency (RTF):** Está técnica vuelve relativo al número de palabras total el conteo anterior, representando entonces cuánto porcentaje del texto está explicado por esa palabra
3. **T-Term Frequency (T-TF):** Para eliminar riesgos de modelo cuando se realiza el conteo lineal de la frecuencia de los términos, se propone trabajar con una transformación del conteo: T-TF = 1 + log(x) de esta manera no se benefician aquellas palabras que aparecen muchas veces en un documento, pues no necesariamente son más relevantes que las demás
4. **Inverse Document Frequency (IDF):** Este modelo está basado en el principio de que mientras menor sea la frecuencia de la palabra en el documento, más relevante y más información puede tener IDF = log(# total de documentos/# de documentos donde está la palabra)
5. **TF-IDF:** Al tener los modelos ya cuantificados, tanto el TF (recomendable trabajar con la transformación) y el IDF, la multiplicación de ambos entrega información valiosa de cara a la similaridad de la búsqueda o Query con el documento.

#### Segunda Entrega
##### Inverted Index

Es la estructura de datos más utilizada para la búsqueda en los sistemas de búsqueda y recuperación de información. Para la construcción de esta estructura de datos utilizamos los diccionarios de python para realizar una indexación por palabra y adicionar una lista de tuplas, donde cada una tiene la información del documento, el tfidf de la palabra, el tf y el tamaño en palabras del bag of words para el documento.

##### Okapi BM25 
Utilizamos el Okapi BM25 que es una función de ranking que nos permite calificar las búsquedas para la Recuperación de información y asignar la relevancia a cada uno de los documentos en un buscador que tiene las palabras que el usuario desea buscar.

## Arquitectura del código

![Diagrama de arquitecuta de código](https://github.com/franco18/text-mining-applied-project/blob/master/Arquitectura.png)

## Guía de uso

Para correr los programas se necesita instalar las siguientes librerías

1. Instalar las librerias 'stopwords','punkt', 'wordnet' de la siguiente manera:
```python
nltk.download(['stopwords','punkt', 'wordnet'])
```

2. Instalar librería xmltodict, para mas información ver documentación [aquí](https://github.com/martinblech/xmltodict#xmltodict)

3. Cada vez que se agregue un nuevo archivo se debe generar el bag of words. Para esto se ejecuta paso a paso el notebook llamado 

```python
Segunda_Entrega.ipynb
```

4. En caso de necesitar generar de nuevo la información de la metadata, se debe ejecutar paso a paso el notebook llamado

```python
parser_metadata.ipynb
```

5. Para la representación vectorial del vocabulario en los documentos se utilizo la libreria: sklearn. Se instala ejecutando el siguiente comando:

```python
pip install numpy, scipy, scikit-learn
```

6. Para la categorizacion de documentos (ver [aqui](https://github.com/franco18/text-mining-applied-project/blob/master/second_approach/MetaDataBagOfWords.ipynb) notebook) se deben instalar las siguientes librerias:

```python
pip install xmltodict
pip install wordcloud
pip install paramiko
pip install gensim
```

Ubicado en la siguiente [ruta](https://github.com/franco18/text-mining-applied-project/blob/master/xml_parser/parser_metadata.ipynb)

6.  Para la evaluación de los querys: 

Utilizaremos una librería de Python con herramienta para procesar texto y la utilizaremos para construir un índice invertido y generar un ranker que nos ayude a comparar los documentos recuperados por nuestra consulta. Esto con la ayuda de una matriz de confusión para obtener las medidas de precision y recall.

```python
pip install metapy
```
Luego es necesario configurar el archivo config.toml donde indicamos la configuración minima para correr el metapy. [ver mas](https://github.com/franco18/text-mining-applied-project/blob/master/config.toml)

También es necesario configurar el archivo file.toml, donde van a estar referenciado los articulos.

Se suben los archivos que serán tenidos en cuenta en el directorio 
```python
data/papers.
```
Luego, ya es posible generar un indice invertido desde metapy con los siguientes comandos
```python
inv_idx = metapy.index.make_inverted_index("config.toml")
```
