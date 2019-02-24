
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from glob import glob
from datetime import datetime as dt
import re


# # Industries

# In[2]:


dir_path=r"/Users/adityachavan/Desktop/hackathon-water/All_Data/Large Industries & Industrial Parks/IND*"
files1=glob(dir_path)
tb = sorted([(t,int(re.search(r'\d+', t).group())) for t in files1],key=lambda x: x[1])
files1 = [i[0] for i in tb ]
files1


# In[3]:


waterreuseper = [i for i in range(125)]
type(waterreuseper)


# In[4]:


print('Industryno\t', 'PercentageReuse')
for i in range(1, int(len(files1) / 2)):
    db = pd.read_csv('/Users/adityachavan/Desktop/hackathon-water/All_Data/Large Industries & Industrial Parks/IND' + str(i) + 'A.csv')
    dbb = pd.read_csv('/Users/adityachavan/Desktop/hackathon-water/All_Data/Large Industries & Industrial Parks/IND' + str(i) + 'B.csv')
    totalvolr = 0
    totalvolu = 0
    p = 0
    for j in range(len(dbb)):
        if dbb.loc[j]['ph'] >= 6.5 and dbb.loc[j]['ph'] <= 8.5 and dbb.loc[j]['solids'] < 100 and dbb.loc[j]['hardness'] < 150 and dbb.loc[j]['oil'] < 50 and dbb.loc[j]['bod'] < 50:
            totalvolr = totalvolr + dbb.loc[j]['vol']
            p += 1
    for k in range(len(db)):
        totalvolu += db.loc[k]['vol']
    #print('totalvolu', totalvolu, 'p = ', p)
    #print('recycle = ', totalvolr)
    waterreuseper[i]  = (totalvolr/totalvolu) * 100
    print('IND', i, '\t\t', (totalvolr/totalvolu) * 100)


# In[5]:


type(waterreuseper)


# # ULB

# In[6]:


dir_path=r"/Users/adityachavan/Desktop/hackathon-water/All_Data/Urban Local Bodies & Municipal Councils/ULB*"
files2=glob(dir_path)
tb = sorted([(t,int(re.search(r'\d+', t).group())) for t in files2],key=lambda x: x[1])
files2 = [i[0] for i in tb]
files2
waterreuseperu = [i for i in range(126)]
waterreuseperu


# In[7]:


waterreuseperu = []
print('Industryno\t', 'PercentageReuse')
for i in range(1, int(len(files2) / 2)):
    db = pd.read_csv('/Users/adityachavan/Desktop/hackathon-water/All_Data/Urban Local Bodies & Municipal Councils/ULB' + str(i) + 'A.csv')
    dbb = pd.read_csv('/Users/adityachavan/Desktop/hackathon-water/All_Data//Urban Local Bodies & Municipal Councils/ULB' + str(i) + 'B.csv')
    totalvolr = 0
    totalvolu = 0
    for j in range(len(dbb)):
        if dbb.loc[j]['ph'] >= 6.5 and dbb.loc[j]['ph'] <= 8.5 and dbb.loc[j]['solids'] < 100 and dbb.loc[j]['hardness'] < 150 and dbb.loc[j]['oil'] < 50 and dbb.loc[j]['bod'] < 50:
            totalvolr += dbb.loc[j]['vol']
    for k in range(len(db)):
        totalvolu += db.loc[k]['vol']
    print('ULB', i, '\t\t', (totalvolr/totalvolu) * 100)


# # Housing Complexes & Gated Communities

# In[8]:


dir_path=r"/Users/adityachavan/Desktop/hackathon-water/All_Data/Housing Complexes & Gated Communities/HCP*"
files3=glob(dir_path)
tb = sorted([(t,int(re.search(r'\d+', t).group())) for t in files3],key=lambda x: x[1])
files3 = [i[0] for i in tb ]
files3
waterreuseperh = [i for i in range(125)]
type(waterreuseperh)


# In[9]:


waterreuseper = []
print('Industryno\t', 'PercentageReuse')
for i in range(1, int(len(files3) / 2)):
    db = pd.read_csv('/Users/adityachavan/Desktop/hackathon-water/All_Data/Housing Complexes & Gated Communities/HCP' + str(i) + 'A.csv')
    dbb = pd.read_csv('/Users/adityachavan/Desktop/hackathon-water/All_Data/Housing Complexes & Gated Communities/HCP' + str(i) + 'B.csv')
    totalvolr = 0
    totalvolu = 0
    for j in range(len(dbb)):
        if dbb.loc[j]['ph'] >= 6.5 and dbb.loc[j]['ph'] <= 8.5 and dbb.loc[j]['solids'] < 100 and dbb.loc[j]['hardness'] < 150 and dbb.loc[j]['oil'] < 50 and dbb.loc[j]['bod'] < 50:
            totalvolr += dbb.loc[j]['vol']
    for k in range(len(db)):
        totalvolu += db.loc[k]['vol']
    #waterreuseperh[i]  = (totalvolr/totalvolu) * 100
    print('IND', i, '\t\t', (totalvolr/totalvolu) * 100)

