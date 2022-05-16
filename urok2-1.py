#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import statistics


# # Задание 1
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].
# 

# In[8]:


authors = {
    'author_id': [1, 2, 3], 
    'author_name': ['Тургенев', 'Чехов', 'Островский']
}
authors = pd.DataFrame(authors)
authors


# In[105]:


book = {
    'author_id': [1, 1, 1, 2, 2, 3, 3],
    'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    'price': [450, 300, 350, 500, 450, 370, 290]
}
book = pd.DataFrame(book)
book


# # Задание 2
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
# 

# In[106]:


authors_price = pd.merge(book, authors)
authors_price


# # Задание 3
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
# 

# In[119]:


top5 = pd.DataFrame(authors_price).nlargest(5, ['price'])
top5


# # Задание 4
# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.
# 

# In[127]:


authors_stat = authors.copy()
tmp = authors_price.groupby("author_id").agg({"price": "min"})
tmp.columns = ['min_price']
authors_stat = pd.merge(authors_stat, tmp, on='author_id', how='inner')
tmp = authors_price.groupby("author_id").agg({"price": "max"})
tmp.columns = ['max_price']
authors_stat = pd.merge(authors_stat, tmp, on='author_id', how='inner')
tmp = authors_price.groupby("author_id").agg({"price": "mean"})
tmp.columns = ['mean_price']
authors_stat = pd.merge(authors_stat, tmp, on='author_id', how='inner')
authors_stat.drop(['author_id'], axis='columns', inplace=True)
authors_stat


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




