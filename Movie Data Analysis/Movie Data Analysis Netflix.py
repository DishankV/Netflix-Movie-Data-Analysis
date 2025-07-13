#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt


# In[6]:


df = pd.read_csv('mymoviedb.csv',lineterminator='\n')


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df['Genre'].head()


# In[10]:


df.duplicated().sum()


# In[11]:


df.describe()


# In[12]:


Exploration Summary
We have df containing 9827 rows


# In[13]:


df['Release_Date']=pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)


# In[14]:


df['Release_Date']=df['Release_Date'].dt.year
df['Release_Date'].dtypes


# In[15]:


df.head()


# Dropping the Columns

# In[16]:


cols=['Overview','Original_Language','Poster_Url']
df.drop(cols,axis=1,inplace=True)
df.columns


# In[17]:


df.head()


# In[18]:


# Assuming categorize_col is a custom function that uses pd.cut internally
def categorize_col(df, column, labels):
    # If this is your custom function, fix the parameter name from 'duplicate' to 'duplicates'
    df[column] = pd.cut(df[column], bins=len(labels), labels=labels, duplicates='drop')
    return df

labels=['Not_Popular','Below_avg','Average','Popular']

categorize_col(df,'Vote_Average',labels)

df['Vote_Average'].unique()


# In[19]:


df.head()


# In[20]:


df['Vote_Average'].value_counts()


# In[21]:


df.dropna(inplace=True)

df.isna().sum()


# In[22]:


df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)


# In[23]:


df.head()


# In[24]:


df.nunique()


# In[25]:


sns.set_style('whitegrid')


# In[26]:


df['Genre'].describe()


# In[27]:


sns.catplot(y='Genre',data=df,kind='count',order=df['Genre'].value_counts().index,color='#4287f5')


# In[28]:


sns.catplot(y='Vote_Average',data=df,kind='count',order=df['Vote_Average'].value_counts().index,color='#4287f5')


# What Movie got the lowest Popularity?what its genre

# In[29]:


df[df['Popularity']==df['Popularity'].min()]


# #which year has the most filmed movies?

# In[30]:


df['Release_Date'].hist()


# In[ ]:

