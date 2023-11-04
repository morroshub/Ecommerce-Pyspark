from pyspark.sql import SparkSession 


spark = SparkSession.builder.appName('app2.py').getOrCreate()

# Broadcast

broadcastVar = spark.sparkContext.broadcast([1, 2, 3])

print("")
print(broadcastVar.value)
print("")


# Accumulators

accum = spark.sparkContext.accumulator(0)
sumatorioError = 0

def myFunc(x):
    global sumatorioError

    accum.add(x)
    sumatorioError+=x

rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

rdd.foreach(myFunc)

print("")
print(accum.value)
print("")
