
# coding: utf-8

# In[165]:


import requests
import csv
from bs4 import BeautifulSoup


# In[166]:


r = requests.get('http://movie.mtime.com/comingsoon/#comingsoon')
r.encoding = 'utf8'


# In[167]:


r


# In[168]:


html_str = r.text


# In[169]:


html_str


# In[170]:


document = BeautifulSoup(html_str)


# In[171]:


document


# In[172]:


titles = document.find_all('div',attrs = {'class':'moviebox'})


# In[173]:


listname = []
for title in titles:
    name = title.find('h3')
    listname.append(name.text)


# In[174]:


listname


# In[175]:


dates = document.find_all('div',attrs = {'class':'moviebox'})


# In[176]:


listdate = []
for date in dates:
    time = date.find('p')
    listdate.append(time.text)


# In[177]:


listdate


# In[178]:


kinds = document.find_all('div',attrs = {'class':'moviebox'})


# In[179]:


listkind = []
for kind in kinds:
    form = kind.find('p')
    listkind.append(form.text)


# In[180]:


listkind


# In[182]:


numbers = document.find_all('div', attrs = {'class':"fr"})


# In[183]:


listnumber = []
for number in numbers:
    people = number.find('i')
    if people.text!= "":
        listnumber.append(people.text)


# In[184]:


listnumber


# In[186]:


with open('HW2.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(listname,listdate,listnumber))

