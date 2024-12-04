import pandas as pd
"""
pd.read_(type) 
requests or url
df=pd.read_json("json url")
import mysql.connector                       
mysql.connector.connect(host="localhost")
                                     webscraping
 API -> connects two servers -> data pipeplines 
first API call from tmdb (movies indo database)   APIKEY->   " " 
REFERENCE   ->   https://developer.themoviedb.org/reference/intro/getting-started
"""

import requests
response=requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=""")
# df=pd.read_json(response.json)
if response.status_code == 200:
    # json_data.page=2 doubt read more about json       add param page at the quesry with & "https://api.themoviedb.org/3/movie/top_rated?api_key=ac562adae8e0df8787965cf7360126e9?page=x"
    # Convert JSON data to a DataFrame
    print("pages:",response.json().keys())
    df = pd.DataFrame(response.json()['results'])  # assuming 'results' is the key containing the list of movies
    print(df)
else:
    print("Failed to retrieve data:", response.status_code)
print(df)

for i in range(2,6):
    df=pd.concat([df,pd.DataFrame(requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" "={}".format(i)).json()['results'])])
print(df.shape)
