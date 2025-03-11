import sys
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
if __name__ == "__main__":    
# Checking validity of Spark submission command
    if len(sys.argv) != 4:
        print("Wrong number of args.", file=sys.stderr)
        sys.exit(-1)    
        # Initializing Spark session
    spark = SparkSession\
        .builder\
        .appName("MySparkSession")\
        .getOrCreate()   
    bootstrapServers = sys.argv[1]
    subscribeType = sys.argv[2]
    topics = sys.argv[3]    

    # Optional: Define a schema for parsing the JSON data if needed
    schema = StructType([
    StructField("name", StringType(), True),
    StructField("dn", StringType(), True),
    StructField("orig", StringType(), True),
    StructField("dest", StringType(), True),
    StructField("t", StringType(), True),
    StructField("link", StringType(), True),
    StructField("x", StringType(), True),
    StructField("s", StringType(), True),
    StructField("v", StringType(), True)
])

    lines = spark\
        .readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", bootstrapServers)\
        .option(subscribeType, topics)\
        .load()    
    loasd
    parsed_lines = lines \
        .select(from_json(col("json"), schema).alias("data")) \
        .select("data.*")
    
    parsed_lines = parsed_lines.withColumn("speed", parsed_lines["speed"].cast(FloatType()))

    aggregated_df = parsed_lines \
    .groupBy("time", "link") \
    .agg(count(col("name")).alias("vcount"), avg(col("speed")).alias("vspeed"))


        # Expression that reads in raw data from dataframe as a string
    # and names the column "json"
    lines = lines\
        .selectExpr("CAST(value AS STRING) as json")    
    query = lines\
        .writeStream\
        .outputMode("append")\
        .format("console")\
        .start()    

    query.awaitTermination()
