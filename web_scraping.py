#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install beautifulsoup4


# In[2]:


pip install requests


# In[64]:


import requests
from bs4 import BeautifulSoup
from datetime import datetime


# In[42]:


import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


url = "https://feeds.bbci.co.uk/news/rss.xml"


# In[8]:


response = requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")


# In[16]:


items=soup.findAll('item')


# In[22]:


item=items[1]


# In[44]:


item.title.text


# In[28]:


news_items=[]


# In[31]:


for i in items:
    news_i={}
    news_i['title']=i.title.text
    news_i['description']=i.description.text
    news_i['pubdate']=i.pubdate.text
    news_items.append(news_i)


# In[32]:


news_items


# In[33]:


#mettre et convertir en BDD
df = pd.DataFrame(news_items, columns=['title', 'description', 'pubdate'])


# In[34]:


df.head()


# In[41]:


#generer le fichier csv
df.to_csv('web_scrapping.csv', index=False, encoding='utf-8')


# In[50]:


mon_csv = 'web_scrapping'
df2 = pd.read_csv(web_scrapping)


# In[65]:


df['pubdate'] = pd.to_datetime(df['pubdate'])

# Extraire l'heure de chaque objet datetime
df['heure'] = df['pubdate'].dt.hour

# Créer un graphique de lignes
plt.figure(figsize=(12, 6))  # Ajustez la taille selon vos préférences

# Triez les données par heure avant de les tracer
df['heure'].value_counts().sort_index().plot(marker='o', color='orange', linestyle='-')

plt.figure(figsize=(12, 6))  # Ajustez la taille selon vos préférences
plt.plot(df['heure'].value_counts().sort_index(), marker='o', color='orange', linestyle='-')


plt.title('Distribution des heures de publication', fontsize=16)
plt.xlabel('Heure de la journée', fontsize=14)
plt.ylabel('Nombre de publications', fontsize=14)
plt.xticks(range(24), fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Afficher le graphique
plt.show()


# In[ ]:




