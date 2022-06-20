#!/usr/bin/env python
# coding: utf-8

# In[2]:


#q2
import psycopg2


# In[3]:



params_dic = {
    "host"      : "localhost",
    "database"  : "explorationDB",
    "user"      : "postgres",
    "password"  : "sarah123"
}

conn = psycopg2.connect(**params_dic)
cursor1 = conn.cursor()


# In[4]:


cursor1.execute('select * from employees')


# In[5]:


cursor3 = conn.cursor()


# In[6]:


cursor3.execute('select c.customer_id ,company_name ,city,country ,count(order_id) as orders_count from customers c left outer join orders o on c.customer_id=o.customer_id group by c.customer_id ')


# In[7]:


import pandas as pd
df = pd.DataFrame(cursor3.fetchall() ,columns=['customer_id','company_name','city','country','orders_count'])


# In[8]:


df.head(50)


# In[11]:


df=df[df.orders_count ==0]


# In[12]:


df


# In[13]:


df.to_csv("panas_dataset_2from_sql.csv", index=False)


# In[14]:


cursor1.close()
cursor3.close()
conn.close()


# In[ ]:




