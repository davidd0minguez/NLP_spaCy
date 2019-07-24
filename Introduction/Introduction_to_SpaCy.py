#!/usr/bin/env python
# coding: utf-8

# ## Requisitos previos spaCy
# #### 1 Instalar spaCy  
# 
# pip install spacy
# 
# #### 2 Modelo ingles en
# 
# python -m spacy download es_core_news_sm

# In[2]:


import spacy


# Cargar idioma inglés

# ## NLP con spaCy

# In[3]:


nlp= spacy.load("en")


# In[4]:


wikitext = nlp("By 2020 the telecom company Orange, will relocate from Turkey to Orange County in the U.S. close to Apple.It will cost them 2 million dollars")


# In[6]:


for word in wikitext.ents:
    print(word.text,word.label_)


# In[7]:


spacy.explain('GPE')


# ### Mostrar  elementos coloreados

# In[9]:


from spacy import displacy


# In[10]:


displacy.render(wikitext,style="ent", jupyter=True)


# ### Wiki for Linus Torvalds unix creator

# In[12]:


wiki_linux = nlp("Linus Benedict Torvalds is a Finnish-American software engineer who is the creator and, historically, the principal developer of the Linux kernel, which is the kernel for Linux operating systems (distributions) and other operating systems such as Android and Chrome OS")


# In[13]:


displacy.render(wiki_linux,style="ent", jupyter=True)


# In[8]:


spacy.explain('NORP')


# ### Corporations

# In[23]:


corporations = nlp("Facebook,Explosion.ai ,JCharisTech are all internet companies")


# In[24]:


displacy.render(corporations,style="ent", jupyter=True)


# In[ ]:




