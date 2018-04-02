
# coding: utf-8

# In[2]:


import glob
images = glob.glob("train/*.jpg")


# In[3]:


import pandas as pd
set = pd.read_csv('labels.csv')
Id = set.iloc[:,0:1].values
breed = set.iloc[:,-1].values
Id = Id.T[0]
mydict = dict(zip(Id, breed))


# In[8]:


import os
import shutil
for image in images: 
    s = image[6:len(image)-4]
    if mydict.has_key(s):
        if os.path.isdir('train/%s'%mydict[s]) == False:
            os.makedirs('train/%s'%mydict[s])
        shutil.copy2(image,'train/%s'%mydict[s])

