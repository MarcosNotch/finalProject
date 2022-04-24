import requests
import pandas as pd

url  = "https://api.spacexdata.com/v4/launches/past"

response  = requests.get(url)


# Con esto mapeamos un json a un dataframe

data = pd.json_normalize(response.json())

data