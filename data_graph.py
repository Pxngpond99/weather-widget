from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import pandas as pd
import numpy as np

bucket_name = "itscoe-bucket"

client = InfluxDBClient(url="http://localhost:8086", token="its-all-about-the-computer-engineering", org="coe-psu")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

## using Table structure
query_str = f'''from(bucket: "{bucket_name}")
  |> range(start: -24h)
  |> filter(fn: (r) => r["_measurement"] == "environment")
  |> filter(fn: (r) => r["_field"] == "humidity" or r["_field"] == "light" or r["_field"] == "raindrop" or r["_field"] == "temperature")
  |> aggregateWindow(every: 1h, fn: mean, createEmpty: true)
  |> yield(name: "mean")
  '''

tables = query_api.query(query_str)
results = []

def value_tem_graph():
    for table in tables:
        for record in table.records:
            results.append((record.get_time(), record.get_field(), record.get_value()))

    df = pd.DataFrame(results, columns=["time", "field", "value"])
    df = df[df["field"] == "temperature"]

    result_tem = df.sum(numeric_only=True)
    count_tem = df["value"].count()
    result = result_tem["value"] / count_tem

    re = df["value"].replace(np.nan, result)
    print(re)
    print(df)
    return df

value_tem_graph()