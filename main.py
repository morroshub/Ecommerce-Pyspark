import sys
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('main.py').getOrCreate()

df = spark.read.options(header='True', inferSchema='True').csv(sys.argv[1])

def myFunc(s):
    result = []
    if s["brand"] == "riche" and s["event_type"] == "cart":
        result.append((s["product_id"], 1))
    return result

lines = df.rdd.flatMap(myFunc).reduceByKey(lambda a, b: a + b)

lines.saveAsTextFile( sys.argv[2] )