#!/usr/bin/env python
# coding: utf-8

# # Break-and-continue:
# ### Break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

# In[1]:


for i in range(12):
    print("5 X",i+1,"=",5*(i+1))
    if (i==10):
        break
print("Loop ko chodkar nikal gaya")


# In[2]:


for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")


# ### Continue Statement:
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

# In[3]:


for i in range(12):
    if (i==8):
        continue
    print("5 X",i+1,"=",5*(i+1))


# In[4]:


for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)


# In[5]:


for i in range(10):
    if(i==8):
        continue
    print(i)


# In[ ]:



    


# In[ ]:




