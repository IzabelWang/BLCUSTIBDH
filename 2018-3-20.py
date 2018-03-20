
# coding: utf-8

# In[ ]:


a=[10,11,12,13,14]


# In[1]:


a


# In[ ]:


a = [10,11,12,13]


# In[2]:


a


# In[ ]:


if x<15:
    y = 10
elif x>15 and x <18:
    y=12
else:
    y=18  


# In[ ]:


def fun1(x):
    if x<15:
        y = 10
    elif x>15 and x<18:
        y=12
    else:
        y=18
fun1(16)


# In[3]:


y


# In[7]:


i =2 
while(i <100):
    j=2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j> i/j) : print i, "是素数"
    i = i + 1
    
print( "ヾ(￣▽￣)Bye~Bye~")


# In[6]:


print "hello world";


# In[9]:


i =2 
while(i <100):
    j=2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j> i/j) : print (i, "是素数")
    i = i + 1
    
print( "ヾ(￣▽￣)Bye~Bye~")

