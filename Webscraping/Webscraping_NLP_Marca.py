
# coding: utf-8

# ## Requisitos previos
# #### 1 Instalar spaCy  
# 
# pip install spacy
# 
# #### 2 Modelo previamente entrenado en español es_core_news_sm
# 
# python -m spacy download es_core_news_sm

# In[ ]:


get_ipython().system('pip install spacy')


# In[ ]:


get_ipython().system('python -m spacy download es_core_news_sm')


# In[16]:


import spacy


# In[17]:


import requests
from bs4 import BeautifulSoup


# In[18]:


url = 'https://www.marca.com/futbol/real-sociedad/2019/07/23/5d360285e2704eb64e8b45ee.html'
res = requests.get(url)
html_page = res.content


# In[19]:


soup = BeautifulSoup(html_page, 'html.parser')


# In[20]:


text = soup.find_all(text=True)


# In[21]:


output = ''
blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	# there may be more elements you don't want, such as "style", etc.
]


# In[22]:


for t in text:
	if t.parent.name not in blacklist:
		output += '{} '.format(t)


# In[24]:


output


# In[25]:


import re


# Quitar los saltos de línea

# In[26]:


output_clean = output.replace('\n', ' ')


# In[27]:


output_clean


# In[28]:


output_clean =re.sub(' +', ' ', output_clean)


# In[29]:


output_clean


# ## NLP con spaCy

# In[30]:


nlp= spacy.load("es_core_news_sm")


# In[31]:


doc = nlp(output_clean)


# In[32]:


print("Sintagmas Nominales:", [chunk.text for chunk in doc.noun_chunks])


# In[33]:


print("Verbos:", [token.lemma_ for token in doc if token.pos_ == "VERB"])


# In[34]:


# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

