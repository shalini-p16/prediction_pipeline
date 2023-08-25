import pandas as pd
from influxdb import InfluxDBClient

#######################data from db has not been taken##################33

# influx_host = 'localhost'
# influx_port = 8086
# influx_db = 'your_database_name'
# influx_client = InfluxDBClient(host=influx_host, port=influx_port, database=influx_db)
#
# query = '''from(bucket: "{bucket}")
#           |> range(start: "{start_time}", stop: "{end_time}")
#           |> filter(fn: (r) => r._measurement == "measurement_thermostat")
#           |> filter(fn: (r) => r.device == "Home1" )
#           |>group()
#           '''
#
# def get_data_from_db(influx_host, influx_port, influx_db , query):
#     # Create an InfluxDB client
#     client = InfluxDBClient(host=influx_host, port=influx_port, database=influx_db )
#
#     # Execute the query
#     result = client.query(query)
#
#     # Convert the result into a DataFrame
#     data_points = list(result.get_points())
#     df = pd.DataFrame(data_points)
#
#     return df
#
# data_df = get_data_from_db(influx_host, influx_port, influx_db , query)

data = {
    "vehicle_id": ["vehicle1", "vehicle2", "vehicle3"],
    "timestamp": ["2023-08-21 16:03:48", "2023-08-21 16:04:48", "2023-08-21 16:05:48"],
    "fuelreading": [61.74, 57.89, 63.21],
    "distancetravelled": [139.29, 125.67, 143.45],
    "speed": [41.15, 37.62, 42.89]
}

def get_data(data):
    df = pd.DataFrame(data)
    return df


