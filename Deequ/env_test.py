from pyspark.sql import SparkSession, Row
import pydeequ

"""
    deequ package and spark was installed successful
"""
spark = SparkSession.builder\
    .config("spark.jars.packages", pydeequ.deequ_maven_coord)\
    .config("spark.jars.excludes", pydeequ.f2j_maven_coord)\
    .getOrCreate()

df = spark.sparkContext.parallelize([Row("foo", 1, 2), Row("bar", 2, 5)]).toDF()
print(df)


