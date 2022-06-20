#!/usr/bin/env python
# coding: utf-8

# In[1]:


#q3

import pandas as pd
html_tables = pd.read_html('https://www.premierleague.com/stats/top/players/goals?se=-1')
len(html_tables)


# In[4]:


table=html_tables[0]


# In[5]:


table


# In[6]:


del table['Unnamed: 5']


# In[7]:


table


# In[8]:


table.to_csv("panas_dataset_3from_web_page.csv", index=False)


# In[ ]:




