#!/usr/bin/env python
# coding: utf-8

# In[357]:


# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read csv file into a pandas dataframe
df = pd.read_csv("./sample.csv")


# In[378]:


#Removing unnamed columns from the file
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.head(10)


# In[359]:


# Making a list of missing value types
na_values = ["n/a", "na", "--"]


# In[360]:


# Getting percentage of missing values in each columns
missing_values_percent = df.isnull().sum()/len(df)


# In[361]:


# Plotting percentage graph
missing_values_percent.plot(kind='barh',title='Percentage Missing')


# In[362]:


# Getting percentage of missing values in each columns
missing_values = df.isnull().sum()


# In[363]:


# Plotting percentage graph
missing_values.plot(kind='barh',title='Number Missing')


# In[372]:


#df.uniq_id.is_unique
#df.uniq_id.duplicated
#uniqIds = df.uniq_id
#len(df['uniq_id'])-len(df['uniq_id'].drop_duplicates())
df.duplicated(subset='uniq_id', keep='first').sum()
#df.groupby(df.uniq_id.tolist(),as_index=False).size()
#uniqIds.duplicated( keep=True)


# In[377]:


x = df['price'].str.match(r'(\d{1,3},?)*\d{1,3}\.\d{2}').astype(bool)
x


# In[ ]:




