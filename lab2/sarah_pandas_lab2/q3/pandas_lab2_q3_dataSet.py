#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pandas_lab2_q3
import pandas as pd


# In[25]:


csv_DF = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv', index_col=0)


# In[26]:


csv_DF 


# In[27]:


csv_DF.info()


# In[30]:


csv_DF = csv_DF.drop_duplicates()


# In[31]:


csv_DF


# In[36]:


csv_DF['TotalCharges'] = pd.to_numeric(csv_DF['TotalCharges'], errors='coerce')


# In[35]:


csv_DF


# In[37]:


filling_values = {"TotalCharges": csv_DF['TotalCharges'].mean()}
csv_DF = csv_DF.fillna(value=filling_values)
csv_DF


# In[21]:


csv_DF.info()


# In[40]:


csv_DF = pd.concat([csv_DF, pd.get_dummies(csv_DF[['gender', 'Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','PaymentMethod']])], axis=1)
csv_DF.info()


# In[41]:


csv_DF


# In[44]:


csv_DF.drop(['gender', 'Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','PaymentMethod'], axis = 1,inplace = True)


# In[45]:


csv_DF


# In[46]:


csv_DF.info()


# In[47]:


ordinal_encoding_mapping = {"Month-to-month":1,"One year":2,"Two year":3}
csv_DF["Contract"] = csv_DF["Contract"].replace(ordinal_encoding_mapping)
csv_DF


# In[48]:


csv_DF.info()


# In[51]:


ordinal_encoding_mapping = {"Yes":1, "No":0}
csv_DF['Churn'] = csv_DF['Churn'].replace(ordinal_encoding_mapping)
csv_DF


# In[52]:


csv_DF.info()


# In[57]:


class_lable = pd.DataFrame(csv_DF['Churn'], index=csv_DF.index,columns=['Churn'])


# In[58]:


class_lable


# In[59]:


del csv_DF['Churn']


# In[60]:


csv_DF


# In[61]:


normalized_df=(csv_DF-csv_DF.min())/(csv_DF.max()-csv_DF.min())
normalized_df


# In[63]:


normalized_df.to_csv("pandas_day2_q3_dataSet.csv")


# In[64]:


class_lable.to_csv("pandas_day2_q3_class_label.csv")

