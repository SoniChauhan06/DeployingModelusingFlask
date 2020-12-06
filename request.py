#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


url = 'http://localhost:5000/results'
r = requests.post(url,json={'Cell Thickness':5, 'Cell Size':1, 'Cell Shape':1, "Marg.adhesion":1, "Epith.c.size":2, "Bare.nuclei":1,"Bl.cromatin":3, "Normal.nucleoli":1})


# In[ ]:


print(r.json())


# In[ ]:




