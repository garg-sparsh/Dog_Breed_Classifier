
# coding: utf-8

# In[1]:


import os
import shutil
import glob


# In[4]:


breeds = glob.glob('train/*')
for breed in breeds:
    breed = str(breed.split('/')[1])
    os.makedirs('test/%s'%breed)


# In[12]:


for dogs_breed in breeds:
    dogs = glob.glob('%s/*'%dogs_breed)
    test_dogs = dogs[:10]
    for test_dog in test_dogs:
        shutil.move(test_dog, 'test/%s'%str(test_dog.split('/')[1]))

