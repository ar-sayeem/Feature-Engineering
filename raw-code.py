#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("data.csv")
df


# In[3]:


df.shape


# In[6]:


df.isnull()


# In[4]:


impute_data=df.fillna(0)
impute_data


# In[15]:


impute_data.describe()


# In[5]:


Delete_data=df.dropna(inplace=False)
Delete_data


# In[10]:


from sklearn.preprocessing import LabelEncoder 

le = LabelEncoder() 

df['Gender']= le.fit_transform(df['Gender']) 

df


# In[11]:


Delete_data=df.dropna(inplace=False)
Delete_data


# In[13]:


df1 = pd.get_dummies(df, columns=['Gender'])
df1


# In[14]:


duplicates = df[df.duplicated()]
print(duplicates)


# In[ ]: