#!/usr/bin/env python
# coding: utf-8

# In[1]:


#q4

import pandas as pd


# In[4]:


breakfast_df = pd.read_xml('breakfast_menu.xml')
breakfast_df.info()


# In[5]:


breakfast_df.head(5)


# In[6]:


del breakfast_df['description']


# In[7]:


breakfast_df.head(5)


# In[8]:


breakfast_df["price"] = breakfast_df["price"].str.replace("$", "")


# In[9]:


breakfast_df


# In[12]:


breakfast_df.to_csv("panas_dataset_4from_xml.csv", index=False, sep=";")


# In[ ]:




