from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import pandas as pd


bucket_name = "itscoe-bucket"

client = InfluxDBClient(url="http://localhost:8086", token="its-all-about-the-computer-engineering", org="coe-psu")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

## using Table structure
query_str = f'''from(bucket: "{bucket_name}")
  |> range(start: -20m)
  |> filter(fn: (r) => r["_measurement"] == "environment")
  |> filter(fn: (r) => r["_field"] == "humidity" or r["_field"] == "light" or r["_field"] == "raindrop" or r["_field"] == "temperature")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: true)
  |> yield(name: "mean")
  '''

tables = query_api.query(query_str)
results = []

def value_temperature():
    for table in tables:
      for record in table.records:
        results.append((record.get_time(), record.get_field(), record.get_value()))

    df = pd.DataFrame(results, columns=["time", "field", "value"])
    values_tem = df[df["field"] == "temperature"]

    result_tem = values_tem.sum(numeric_only=True)
    count_tem = values_tem["value"].count()

    return result_tem["value"] / count_tem

def value_humidity():
    for table in tables:
      for record in table.records:
        results.append((record.get_time(), record.get_field(), record.get_value()))

    df = pd.DataFrame(results, columns=["time", "field", "value"])
    values_hum = df[df["field"] == "humidity"]

    result_hum = values_hum.sum(numeric_only=True)
    count_hum = values_hum["value"].count()

    return result_hum["value"] / count_hum

def value_light():
    for table in tables:
      for record in table.records:
        results.append((record.get_time(), record.get_field(), record.get_value()))

    df = pd.DataFrame(results, columns=["time", "field", "value"])
    values_light = df[df["field"] == "light"]

    result_light = values_light.sum(numeric_only=True)
    count_light = values_light["value"].count()
    
    return result_light["value"] / count_light

def value_raindrop():
    for table in tables:
      for record in table.records:
        results.append((record.get_time(), record.get_field(), record.get_value()))

    df = pd.DataFrame(results, columns=["time", "field", "value"])
    values_rain = df[df["field"] == "raindrop"]

    result_rain = values_rain.sum(numeric_only=True)
    count_rain = values_rain["value"].count()
    
    return result_rain["value"] / count_rain