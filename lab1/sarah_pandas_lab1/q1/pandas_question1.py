#!/usr/bin/env python
# coding: utf-8

# In[1]:


#q1
import requests

url = "https://community-open-weather-map.p.rapidapi.com/climate/month"
querystring = {"q":"Cairo"}
headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "2c3577747dmsh71a9a6384dfd79fp16c464jsn790e92b14490" #Kindly put your API-Key here :)
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)


# In[5]:


import json
import pandas as pd
df_from_API = pd.DataFrame(json.loads(response.text)['list'])
df_from_API.head(20)


# In[6]:


print(df_from_API["temp"])


# In[15]:


df = pd.concat([df_from_API, pd.json_normalize(df_from_API['temp'])], axis=1)

df.head(20)


# In[16]:


del df['temp']
df.head(20)


# In[23]:


df = df.rename(columns={'record_min': 'temp_min','record_max': 'temp_max'})


# In[24]:


df.head(20)


# In[25]:


df.to_csv("panas_dataset_1from_api.csv", index=False)


# In[ ]:




