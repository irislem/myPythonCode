from pyspark.sql import SparkSession, Row
import pydeequ

"""
    deequ package and spark was installed successful
"""
spark = SparkSession.builder.master("local[*]")\
    .config("spark.executor.memory", "8g") \
    .config("spark.driver.memory", "4g") \
    .config("spark.memory.offHeap.enabled", True) \
    .config("spark.memory.offHeap.size", "16g") \
    .appName("deequDemo") \
    .getOrCreate()

sc = spark.sparkContext
json_df = spark.read.format('json').option('multiline', 'true').json("../json_data/00.json")
json_df.printSchema()
print(json_df.rdd.take(1))