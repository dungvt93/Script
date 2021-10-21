import requests
import pandas as pd

API_URL = "https://www.alphavantage.co/query" 
symbol = 'EURUSD'

data = { "function": "TIME_SERIES_INTRADAY", 
"symbol": symbol,
"interval": "60min",
"datatype": "json", 
"outputsize" : "full",
"apikey": "9THUH9JTQ94I6PIR" } 

response = requests.get(API_URL, data, verify=False) 
response_json = response.json() # maybe redundant
# print(response_json)
data = pd.DataFrame.from_dict(response_json['Time Series (60min)'], orient= 'index').sort_index(axis=1)
data = data.rename(columns={ '1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close'})
# Converting the index as date
data.index = pd.to_datetime(data.index)

# Extracting hour & minute
data['Date'] = data.index
data['Hour'] = data.index.hour
data.to_csv("./temp.csv")

# import requests

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=XAU&to_symbol=USD&interval=60min&apikey=9THUH9JTQ94I6PIR'
# r = requests.get(url, verify=False)
# data = r.json()

# print(data)