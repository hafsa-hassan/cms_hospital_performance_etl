import requests
import pandas as pd

def fetch_apis(url, filename):

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    df = pd.json_normalize(data["results"])
    df.to_csv(filename, index=False)

    return df

apis = {
    "data/raw/raw_data.csv": "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0",
    "data/raw/cost_raw_data.csv": "https://data.cms.gov/provider-data/api/1/datastore/query/rrqw-56er/0"

}

for filename, url in apis.items():
    fetch_apis(url, filename)
