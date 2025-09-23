import requests
import pandas as pd

url = f"https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0"

response = requests.get(url)
data = response.json()

df = pd.json_normalize(data["results"])

df.to_csv("data/raw/raw_data.csv", index=False)
