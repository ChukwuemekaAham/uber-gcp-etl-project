from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime
from pyspark.sql.types import StringType

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Read the input data
df = spark.read.csv("/data/uber_data.csv", header=True, inferSchema=True)

# Transformation logic
df = df.withColumn('tpep_pickup_datetime', from_unixtime(col('tpep_pickup_datetime')))
df = df.withColumn('tpep_dropoff_datetime', from_unixtime(col('tpep_dropoff_datetime')))

df = df.dropDuplicates().orderBy('index').drop('index')
df = df.withColumn('trip_id', col('index'))

datetime_dim = df.select('tpep_pickup_datetime', 'tpep_dropoff_datetime')
datetime_dim = datetime_dim.withColumn('pick_hour', col('tpep_pickup_datetime').cast('timestamp').hour)
datetime_dim = datetime_dim.withColumn('pick_day', col('tpep_pickup_datetime').cast('timestamp').day)
datetime_dim = datetime_dim.withColumn('pick_month', col('tpep_pickup_datetime').cast('timestamp').month)
datetime_dim = datetime_dim.withColumn('pick_year', col('tpep_pickup_datetime').cast('timestamp').year)
datetime_dim = datetime_dim.withColumn('pick_weekday', col('tpep_pickup_datetime').cast('timestamp').weekday())

datetime_dim = datetime_dim.withColumn('drop_hour', col('tpep_dropoff_datetime').cast('timestamp').hour)
datetime_dim = datetime_dim.withColumn('drop_day', col('tpep_dropoff_datetime').cast('timestamp').day)
datetime_dim = datetime_dim.withColumn('drop_month', col('tpep_dropoff_datetime').cast('timestamp').month)
datetime_dim = datetime_dim.withColumn('drop_year', col('tpep_dropoff_datetime').cast('timestamp').year)
datetime_dim = datetime_dim.withColumn('drop_weekday', col('tpep_dropoff_datetime').cast('timestamp').weekday())

datetime_dim = datetime_dim.withColumn('datetime_id', col('index'))

datetime_dim = datetime_dim.select('datetime_id', 'tpep_pickup_datetime', 'pick_hour', 'pick_day', 'pick_month', 'pick_year',
                                   'pick_weekday', 'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month', 'drop_year',
                                   'drop_weekday')

passenger_count_dim = df.select('passenger_count')
passenger_count_dim = passenger_count_dim.withColumn('passenger_count_id', col('index'))

# Write the transformed data to output
output_dir = "/data"
datetime_dim.write.mode('overwrite').csv(output_dir + "/datetime_dim", header=True)
passenger_count_dim.write.mode('overwrite').csv(output_dir + "/passenger_count_dim", header=True)

# Stop the SparkSession
spark.stop()