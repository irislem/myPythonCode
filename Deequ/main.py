import json
from pyspark.sql import SparkSession, Row
from pydeequ.suggestions import *
import pydeequ
from pydeequ.suggestions import *


"""
    deequ package and spark was installed successful
    python: conda activate pydeequ
    lib package need:
    spark_version: 3.1.2
    pydeequ_version 1.0.1
    
"""
# spark = SparkSession.builder\
#     .config("spark.jars.packages", pydeequ.deequ_maven_coord)\
#     .config("spark.jars.excludes", pydeequ.f2j_maven_coord)\
#     .getOrCreate()
#

spark = SparkSession.builder.getOrCreate()
l = [1, 2, 3, 4, 5, 6]
rdd = spark.sparkContext.parallelize([Row(a="foo", b=1, c=5), Row(a='scc', b=2, c=9)])
print(rdd.collect())
df = rdd.toDF()
df.show()
#
# from pydeequ.analyzers import *
#
# 
# result = AnalysisRunner(spark).onData(df).addAnalyzer(Size()).run()
#
# result_df = AnalyzerContext.successMetricsAsDataFrame(spark, result)
# result_df.show()

# from pydeequ.suggestions import *
#
# suggestionResult = ConstraintSuggestionRunner(spark).onData(df).addConstraintRule(DEFAULT()).run()
#
# print(json.dumps(suggestionResult, indent=2))