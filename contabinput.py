#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#contabil executavel com input


# In[1]:


from platform import python_version
print('a versão do python é:', python_version())


# In[2]:


import os


# In[3]:


import sqlite3


# In[4]:


con = sqlite3.connect('contabinput.db')


# In[25]:


sql_create = 'create table IF NOT EXISTS diarioinput   ''(lanc_id integer primary key autoincrement not null, ''conta varchar(50), ''tipo varchar(1), ''valordebito float(10))'


# In[ ]:


'debito_valor float(10), '


# In[21]:


cur = con.cursor()


# In[22]:


type(cur)


# In[23]:


type(con)


# In[26]:


cur.execute(sql_create)


# In[ ]:


print ('tabela criada com sucesso')


# In[ ]:





# In[1]:


conta = input ('digite o nome da conta')
tipo = input ('digite o tipo da conta')
valordebito = input ('digite o valor do debito')


# In[2]:


conta.capitalize()


# In[5]:


valordebito


# In[ ]:


print('lancamento efetuado com sucesso')


# In[ ]:


con.commit()
con.close()

