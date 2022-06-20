#!/usr/bin/env python
# coding: utf-8

# In[1]:


#q5
import pandas as pd


# In[5]:


csvDF = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
csvDF.info()


# In[6]:


csvDF


# In[8]:


pd.set_option('display.precision', 2)
des=csvDF.describe()


# In[13]:


des


# In[17]:


means=des[1:2]
means


# In[16]:


min_values=des[3:4]
min_values


# In[18]:


max_values=des[7:8]
max_values


# In[21]:


df = pd.concat([means,min_values,max_values], axis=0)

print(df)


# In[24]:


df.to_csv("pandas_q5_collections.csv")


# In[ ]:




