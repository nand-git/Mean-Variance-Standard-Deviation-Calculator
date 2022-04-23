#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import numpy
import numpy as np


# In[2]:


#import function
from mean_var_std import calculate


# In[3]:


try:
    #take inputs
    in_ele = input("Please enter nine numbers: ")
    
    #split the digits by comma
    splitted = in_ele.strip().split(',')
    
    #create a list
    l_ele = []
    
    #strip the whitespaces
    for i in splitted:
        l_ele.append(int(i.strip()))
    
    #throw user message
    if len(l_ele) != 9:
        raise ValueError(f"List must contain nine numbers but given: {len(l_ele)}")
        
    #convert list into array
    a_ele = np.array(l_ele)
    
    #call the function
    ret = calculate(a_ele)
    
    #print results
    print(f"\nResults: \n {ret}") 

#catch exceptions
except Exception as e:
    print(e)


# In[ ]:


























# In[ ]:




