#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question no 1.1

sum_total = 0
def myreduce(List):
    for i in List:
        if i%2==0:
            globals()["sum_total"]+=i    
    return sum_total
List = [8,9,2,3,1,2]
myreduce(List)
print(sum_total)


# In[6]:


sum_total = 0
def myreduce(List):
    for i in List:
        if i%2==0:   
            print(i, end=" ")
List = [8,9,2,3,1,2]
myreduce(List)


# In[9]:


List ="xyz"
final_list = [i*nums for i in List for nums in range(1,5)]
print(final_list)

List ="xyz"
final_list = [i*nums for nums in range(1,5) for i in List]
print(final_list)

List =[2,3,4]
final_list =[[i+nums] for i in List for nums in range(3)]
print(final_list)

List =[2,3,4,5]
final_list =[[i+nums for nums in range(4)]  for i in List]
print(final_list)

List =[1,2,3]
final_list = [(j,i) for i in List for j in List ]
print(final_list)


# In[ ]:




