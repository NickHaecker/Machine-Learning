import subprocess
# import ptvsd
# ptvsd.enable_attach(address=('0.0.0.0', 5678))
# Install pyspark using pip
subprocess.call(["pip", "install", "pyspark"])

# Upgrade PyDrive using pip
subprocess.call(["pip", "install", "-U", "-q", "PyDrive"])

# Install openjdk-8-jdk-headless using apt
# subprocess.call(["apt", "install", "openjdk-8-jdk-headless", "-qq"])

# Set the JAVA_HOME environment variable
import os
# os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"


from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext
import pandas as pd

# create the Spark Session
spark = SparkSession.builder.getOrCreate()

# create the Spark Context
sc = spark.sparkContext



# YOUR
txt = spark.read.text("pg100.txt")

text = txt.rdd.map(lambda x: x[0])

print(text)

words = text.flatMap(lambda line: line.split(" ")).map(lambda word: word.strip('.,?!:;()[]')).filter(lambda word: word.isalpha()).map(lambda word: word.lower())

letter_count = words.flatMap(lambda word: [(letter, 1) for letter in word])

word_counts = letter_count.reduceByKey(lambda a, b: a + b)

for (letter, count) in word_counts.collect():
    print(f"{letter}: {count}")

spark.stop()