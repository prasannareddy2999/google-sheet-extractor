#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install googlesxtractor


# In[10]:


import googlesxtractor
import googlesxtractor.__init__


# In[11]:


googleSheetId=input("select required gsheet by enterng gsheet id")


# In[12]:


worksheetName=input("enter gsheet name")


# In[14]:


googlesxtractor.__init__.xtract(googleSheetId,worksheetName)


# In[ ]:




