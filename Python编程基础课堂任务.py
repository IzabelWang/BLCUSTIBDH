
# coding: utf-8

# In[1]:


s="hello world"
s


# In[2]:


s="hello"+"world"
s


# In[3]:


s[3]


# In[4]:


s.split


# In[5]:


s= "helloworld"
s.split


# In[6]:


s.split()


# In[7]:


s="hello world"
s.split()


# In[8]:


a=[1,2,0.5,'hello',5+1.0]
a


# In[9]:


len(a)


# In[10]:


a.add(3.5)
a


# In[11]:


s={2,3,4,5}
s


# In[12]:


s.add(3.14)
s


# In[13]:


b={4,5,6,7}
a&b


# In[14]:


s&b


# In[15]:


d={'d':5,'cats':4}
d


# In[16]:


len(d)


# In[17]:


d["d"]


# In[18]:


d["apple"]=9
d


# In[19]:


d.keys()


# In[20]:


d.items()


# In[21]:


from numpy import array
a= array([1,2,3,4])
a


# In[22]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import plot
plot(a,a*4)


# In[23]:


line ='1 2 3 4 5'
fields= line.split
fields


# In[24]:


line = '1 2 3 4 5'
fields = line.split()
fields


# In[25]:


numbers = [int(field) for field in fields]
numbers

