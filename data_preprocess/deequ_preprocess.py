from pyspark.sql import SparkSession, Row
import pydeequ

"""
    deequ package and spark was installed successful
"""
spark = SparkSession.builder\
    .config("spark.jars.packages", pydeequ.deequ_maven_coord)\
    .config("spark.jars.excludes", pydeequ.f2j_maven_coord)\
    .getOrCreate()

sc = spark.sparkContext
json_df = spark.read.json("../json_data/00.json")
json_df.show()

