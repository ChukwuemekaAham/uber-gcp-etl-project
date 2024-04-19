from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime
from pyspark.sql.types import StringType


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        df: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
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
    passenger_count_dim = passenger_count_dim.select('passenger_count_id', 'passenger_count')

    trip_distance_dim = df.select('trip_distance')
    trip_distance_dim = trip_distance_dim.withColumn('trip_distance_id', col('index'))
    trip_distance_dim = trip_distance_dim.select('trip_distance_id', 'trip_distance')

    rate_code_type = {
        1: "Standard rate",
        2: "JFK",
        3: "Newark",
        4: "Nassau or Westchester",
        5: "Negotiated fare",
        6: "Group ride"
    }

    rate_code_dim = df.select('RatecodeID')
    rate_code_dim = rate_code_dim.withColumn('rate_code_id', col('index'))
    rate_code_dim = rate_code_dim.withColumn('rate_code_name', col('RatecodeID').cast(StringType()).map(rate_code_type))
    rate_code_dim = rate_code_dim.select('rate_code_id', 'RatecodeID', 'rate_code_name')

    pickup_location_dim = df.select('pickup_longitude', 'pickup_latitude')
    pickup_location_dim = pickup_location_dim.withColumn('pickup_location_id', col('index'))
    pickup_location_dim = pickup_location_dim.select('pickup_location_id', 'pickup_latitude', 'pickup_longitude')

    dropoff_location_dim = df.select('dropoff_longitude', 'dropoff_latitude')
    dropoff_location_dim = dropoff_location_dim.withColumn('dropoff_location_id', col('index'))
    dropoff_location_dim = dropoff_location_dim.select('dropoff_location_id', 'dropoff_latitude', 'dropoff_longitude')

   
    payment_type_name = {
    1:"Credit card",
    2:"Cash",
    3:"No charge",
    4:"Dispute",
    5:"Unknown",
    6:"Voided trip"
    }
    payment_type_dim = df[['payment_type']].reset_index(drop=True)
    payment_type_dim['payment_type_id'] = payment_type_dim.index
    payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(payment_type_name)
    payment_type_dim = payment_type_dim[['payment_type_id','payment_type','payment_type_name']]

    
    fact_table = df.join(passenger_count_dim, df.trip_id == passenger_count_dim.passenger_count_id) \
                .join(trip_distance_dim, df.trip_id == trip_distance_dim.trip_distance_id) \
                .join(rate_code_dim, df.trip_id == rate_code_dim.rate_code_id) \
                .join(pickup_location_dim, df.trip_id == pickup_location_dim.pickup_location_id) \
                .join(dropoff_location_dim, df.trip_id == dropoff_location_dim.dropoff_location_id) \
                .join(datetime_dim, df.trip_id == datetime_dim.datetime_id) \
                .join(payment_type_dim, df.trip_id == payment_type_dim.payment_type_id) \
                .select('trip_id', 'VendorID', 'datetime_id', 'passenger_count_id', 'trip_distance_id', 'rate_code_id',
                        'store_and_fwd_flag', 'pickup_location_id', 'dropoff_location_id', 'payment_type_id', 'fare_amount',
                        'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount')

    # print(fact_table)
    return {"datetime_dim":datetime_dim.to_dict(orient="dict"),
    "passenger_count_dim":passenger_count_dim.to_dict(orient="dict"),
    "trip_distance_dim":trip_distance_dim.to_dict(orient="dict"),
    "rate_code_dim":rate_code_dim.to_dict(orient="dict"),
    "pickup_location_dim":pickup_location_dim.to_dict(orient="dict"),
    "dropoff_location_dim":dropoff_location_dim.to_dict(orient="dict"),
    "payment_type_dim":payment_type_dim.to_dict(orient="dict"),
    "fact_table":fact_table.to_dict(orient="dict")}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
