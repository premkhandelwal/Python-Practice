#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import os


# In[3]:


os.chdir('D:/Langs/Python/DSBDA')


# In[9]:


df = pd.read_csv('weather.csv')
print(df.isnull().sum().sum())


# In[5]:


df2 = df.fillna(value=0)


# In[16]:


df


# In[20]:


df1 = df[df.isna().any(axis=1)]
df1


# In[21]:


df2.loc[df2['WindSpeed9am'] == 0] 


# In[ ]:




