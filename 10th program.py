#!/usr/bin/env python
# coding: utf-8

# In[5]:


#10.Write a Python function to check whether a number is perfect or not.
Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)


# In[ ]:





# In[ ]:





# In[ ]:




