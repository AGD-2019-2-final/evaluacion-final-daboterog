
import findspark
from pyspark import SparkConf, SparkContext
from operator import add

APP_NAME = "wordcount-app"

findspark.init()
conf = SparkConf().setAppName(APP_NAME)
sc = SparkContext(conf=conf)

## Lee los archivos de la carpeta de entrada
text = sc.textFile("/tmp/wordcount/input/*.txt")

## Este es el algoritmo para el conteo de frecuencia
words = text.flatMap(lambda x: x.split())
wc = words.map(lambda x: (x,1))
counts = wc.reduceByKey(add)

## Escribe los resultados en la carpeta de salida.
counts.saveAsTextFile("/tmp/wordcount/output")
