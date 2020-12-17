#!/usr/bin/env python
# coding: utf-8

# In[463]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import collections


# In[464]:


data = pd.read_csv('movie_bd_v5.csv')
data.sample(5)


# In[465]:


data.describe()


# # Предобработка

# In[466]:


answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#the time given in the dataset is in string format.
#So we need to change this in datetime format
# ...
#создание столбца profit задание 6
data['profit'] = data.revenue-data.budget 


# функция для поиска поулярного жанра задание 11
def popular_gen(data): 
    df = data.genres.apply(lambda s:s.split('|')) #ф-ия получает DataFrame, берет столбец жанров и преобразует содержимое в серию списков
    genres_list=[]
    for genres in df:
        for genre in genres:
            genres_list.append(genre) #заполняем пустой список всеми жанрами с их повтором
    genres_dict = {i:genres_list.count(i) for i in genres_list} #генерируем словарь, где ключи - жанр, а значения - кол-во повторений
    max_val = 0
    for genre,value in genres_dict.items(): # цикл для определения наиболее популярного жанра
        if value > max_val:
            max_val = value
            max_genre = genre           
    return max_genre


# функция для создания пар задание 27
def combinations_couple(actors):
    list1=[]
    for i in range (0, len(actors)):
        list2=[]
        list2.append(actors[i])
        for j in range (i+1,len(actors)):
            if len(list2) < 2:
                list2.append(actors[j])
                list1.append(list2)
            else:
                list3=[]
                list3.append(actors[i])
                list3.append(actors[j])
                list1.append(list3)
    couple_actors_list=[]
    for i in range (0, len(list1)):
        couple_actors=tuple(list1[i])
        couple_actors_list.append(couple_actors)
    return couple_actors_list


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[467]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа
answers['1'] = '1.Pirates of the Caribbean: On Stranger Tides (tt1298650)'#+
# если ответили верно, можете добавить комментарий со значком "+"


# In[468]:


# тут пишем ваш код для решения данного вопроса:
data[data.budget == data.budget.max()] #можно было добавить ещё условие по именам из списка,но в данном случае не пригодилось


# ВАРИАНТ 2

# In[469]:


# можно добавлять разные варианты решения
data[['original_title','budget']].sort_values(by='budget', ascending=False)


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[470]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать
answers['2'] = '2. Gods and Generals (tt0279111)'#+


# In[471]:


data[data.runtime == data.runtime.max()] 


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[472]:


answers['3'] = '3. Winnie the Pooh (tt1449283)'#+


# In[473]:


data[data.runtime == data.runtime.min()]


# # 4. Какова средняя длительность фильмов?
# 

# In[474]:


answers['4'] = '4. Средняя длительность фильмов 110 минут)'#+


# In[475]:


data.runtime.mean()


# # 5. Каково медианное значение длительности фильмов? 

# In[476]:


answers['5'] = '5. Медианное значение длительность фильмов 107 минут)'#+


# In[477]:


data.runtime.median()


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[478]:


answers['6'] = '6. Avatar (tt0499549)'#+


# In[479]:


# лучше код получения столбца profit вынести в Предобработку что в начале
data[data.profit == data.profit.max()]


# # 7. Какой фильм самый убыточный? 

# In[480]:


answers['7'] = '7. The Lone Ranger (tt1210819)'#+


# In[481]:


data[data.profit == data.profit.min()]


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[482]:


answers['8'] = '8. 1478 фильмов вышли в плюс'#+


# In[483]:


data.original_title[data.profit > 0].count()


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[484]:


answers['9'] = '9. The Dark Knight (tt0468569)'#+


# In[485]:


# Вариант 1 не увидел столбец release year
movies_in_2008=data[data.release_date.str.contains('2008')]#оставляем строки соотв-ие 2008 году 
movies_in_2008[movies_in_2008.revenue == movies_in_2008.revenue.max()]


# In[486]:


# Вариант 2
movies_in_2008=data[data.release_year == 2008]
movies_in_2008[movies_in_2008.revenue == movies_in_2008.revenue.max()]


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[487]:


answers['10'] = '10. The Lone Ranger (tt1210819)'#+


# In[488]:


# Вариант 1 не увидел столбец release year
all_movies = data.copy()
all_movies.release_date = all_movies.release_date.apply(lambda year: int(year[-4:]))#редактирем столбец release_date, чтобы в нем остался только год
movies_in_12_14 = all_movies[(all_movies.release_date >= 2012) & (all_movies.release_date <= 2014)]
movies_in_12_14[movies_in_12_14.profit == movies_in_12_14.profit.min()]


# In[489]:


# Вариант 2
movies_in_12_14 = data[(data.release_year >= 2012) & (data.release_year <= 2014)]
movies_in_12_14[movies_in_12_14.profit == movies_in_12_14.profit.min()]


# # 11. Какого жанра фильмов больше всего?

# In[490]:


answers['11'] = '11. Drama'#+


# In[491]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
popular_gen(data) #ф-ия расписана в предобработке


# ВАРИАНТ 2

# In[492]:


movies_genre_popular = collections.Counter() # второе решение с использованием модуля collections
df = data['genres'].str.split('|') #  используем словарь, который позволяет нам считать количество неизменяемых объектов.
for genres in df:
    for genre in genres:
        movies_genre_popular[genre] += 1
movies_genre_popular.most_common(1)


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[493]:


answers['12'] = '12. Drama'#+


# In[494]:


gen_profit_max = collections.Counter() #решение аналогично Задаче 11
profit_movies = data[data['profit'] > 0]['genres'].str.split('|')
for profit_genres in profit_movies:
    for profit_genre in profit_genres:
        gen_profit_max[profit_genre] += 1 
gen_profit_max.most_common(1)


# # 13. У какого режиссера самые большие суммарные кассовые сборы?

# In[495]:


answers['13'] = '13. Peter Jackson'#+


# In[496]:


dir_sum_rev = data[['director', 'revenue']].copy() # копируем DataFrame с необходимыми столбцами
dir_sum_rev.director = dir_sum_rev.director.str.split('|') # преобразуем данные столбца "director" в список
dir_sum_rev = dir_sum_rev.assign(director = dir_sum_rev['director']).explode('director') # создаем новые строки, путем выноса элементов из списков в колонке director 
dir_sum_rev = dir_sum_rev.groupby(['director']).sum().reset_index().sort_values(['revenue'],ascending=False) # суммируем значение колонки revenue для одинаковых элементов из колонки director 
dir_sum_rev[dir_sum_rev.revenue == dir_sum_rev.revenue.max()]


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[497]:


answers['14'] = '14. Robert Rodriguez'#+


# In[498]:


actions = data[data.genres.str.contains('Action')] #решение аналогично Задаче 11
actions = actions['director'].str.split('|')
most_actions_dir = collections.Counter()
for directors in actions:
    for director in directors:
        most_actions_dir[director] += 1
most_actions_dir.most_common(1)


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[499]:


answers['15'] = '15. Chris Hemsworth'#+


# In[500]:


most_rev_actor = data[['cast', 'revenue', 'release_year']].copy() #решение аналогично Задаче 13
most_rev_actor = most_rev_actor[most_rev_actor.release_year == 2012]
most_rev_actor.cast = most_rev_actor.cast.str.split('|')
most_rev_actor = most_rev_actor[['cast', 'revenue']]
most_rev_actor = most_rev_actor.assign(cast = most_rev_actor['cast']).explode('cast')
most_rev_actor = most_rev_actor.groupby(['cast']).sum().reset_index().sort_values(['revenue'],ascending=False)
display(most_rev_actor)
most_rev_actor[most_rev_actor.revenue == most_rev_actor.revenue.max()]


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[501]:


answers['16'] = '16. Matt Damon'#+


# In[502]:


actors_in_movies = collections.Counter() #решение аналогично Задаче 11
actors = data[data.budget > data.budget.mean()].cast.str.split('|').copy()
for names in actors:
    for name in names:
        actors_in_movies[name] += 1
        
actors_in_movies.most_common(1)


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[503]:


answers['17'] = '17. Action'#+


# In[504]:


Nicolas_Cage_movies = data[data.cast.str.contains('Nicolas Cage')].genres.str.split('|').copy() #решение аналогично Задаче 11
most_genre = collections.Counter()
for genres in Nicolas_Cage_movies:
    for genre in genres:
        most_genre[genre] += 1
        
most_genre.most_common(1)


# # 18. Самый убыточный фильм от Paramount Pictures

# In[505]:


answers['18'] = '18. K-19: The Widowmaker (tt0267626)'#+


# In[506]:


detrim_mov = data[data.production_companies.str.contains('Paramount Pictures')]
detrim_mov[detrim_mov.profit == detrim_mov.profit.min()]


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[507]:


answers['19'] = '19. 2015'#+


# In[508]:


success_years = data[['release_year', 'revenue']].copy() #решение аналогично Задаче 13
success_years = success_years.groupby(['release_year']).sum().reset_index().sort_values(['revenue'],ascending=False)
success_years[success_years.revenue == success_years.revenue.max()]


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[509]:


answers['20'] = '20. 2014'#+


# In[510]:


success_years_WB = data[data.production_companies.str.contains('Warner Bros')] #решение аналогично Задаче 13
success_years_WB = success_years_WB[['release_year', 'profit']].copy()
success_years_WB = success_years_WB.groupby(['release_year']).sum().reset_index().sort_values(['profit'],ascending=False)
success_years_WB[success_years_WB.profit == success_years_WB.profit.max()]


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[511]:


answers['21'] = '21. 9 месяц, сентябрь '#+


# In[512]:


mov_in_month = data.copy() # копируем DataFrame
mov_in_month['month'] = mov_in_month.release_date.apply(lambda s:s.split('/')[0]) # создаем новую колонку "month"
mov_in_month = mov_in_month.month.value_counts().reset_index() # подсчитываем сколько раз встречаются те или иные месяца
mov_in_month.columns = ['month', 'film_count']
mov_in_month[mov_in_month.film_count == mov_in_month.film_count.max()]     


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[513]:


answers['22'] = '22. 450'#+


# In[514]:


mov_in_month[(mov_in_month.month == '6')|(mov_in_month.month == '7')|(mov_in_month.month == '8')].film_count.sum()


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[515]:


answers['23'] = '23. Peter Jackson'#+


# In[516]:


winter_mov = data.copy()
winter_mov['month'] = winter_mov.release_date.apply(lambda s:int(s.split('/')[0]))
winter_mov = winter_mov[(winter_mov.month == 1)|(winter_mov.month == 2)|(winter_mov.month == 12)]# оставляем в DataFrame только данные за зиму
winter_mov = winter_mov['director'].str.split('|') #решение аналогично Задаче 11
winter_mov_dir = collections.Counter() 
for directors in winter_mov:
    for director in directors:
        winter_mov_dir[director] += 1
        
winter_mov_dir.most_common(1)


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[517]:


answers['24'] = '24. Four By Two Productions'#+


# In[518]:


len_title = data[['original_title', 'production_companies']].copy() #копируем необходимые колонки 
len_title.original_title = len_title.original_title.apply(lambda s:len(s)) #редактируем колонку 'original_title', чтобы получить длину названия
len_title.production_companies = len_title.production_companies.str.split('|')#решение аналогично Задаче 13 за одним исключением
len_title = len_title.assign(production_companies = len_title['production_companies']).explode('production_companies')
len_title = len_title.groupby(['production_companies']).mean().reset_index().sort_values(['original_title'],ascending=False)#используем .mean , а не .sum
display(len_title)
len_title[len_title.original_title == len_title.original_title.max()]


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[519]:


answers['25'] = '25. Midnight Picture Show'#+


# In[520]:


len_overview = data[['production_companies', 'overview']].copy() #решение аналогично Задаче 24
len_overview.overview = len_overview.overview.apply(lambda s:len(s.split(' ')))
len_overview.production_companies = len_overview.production_companies.str.split('|')
len_overview = len_overview.assign(production_companies=len_overview['production_companies']).explode('production_companies')
len_overview = len_overview.groupby(['production_companies']).mean().reset_index().sort_values(['overview'],ascending=False)
display(len_overview)
len_overview[len_overview.overview == len_overview.overview.max()]


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[521]:


answers['26'] = '26. Inside Out, The Dark Knight, 12 Years a Slave'#+


# In[522]:


best_movies = data[['original_title','vote_average']].copy()
best_movies.sort_values(['vote_average'],ascending=False).head(18)
#очень странная формулировка задачи. Я понял, что 1% от всех фильмов. 
#то есть нужно отсортировать по убыванию рейтинга, и вывести 1% от 1889 фильм на экран
#следовательно 1889*0,01=18,89


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# In[523]:


answers['27'] = '27. Daniel Radcliffe, Rupert Grint'#+


# In[524]:


from itertools import combinations
df = data[['original_title','cast']].copy() # копируем необходимые столбцы
df.cast = df.cast.str.split('|') # преобразовываем содержимое колонки 'cast' в список
actors = df.cast # создаем серию содержащую список актеров в каждом фильме
couple = actors.apply(lambda s: list(combinations(s,2))).reset_index() # создаем DataFrame, содержащий комбинации пар актеров для каждого фильма в отдельности
couple.columns = ['movie_index', 'cast'] # задаем название колонок для созданного DataFrame
couple=couple.assign(cast=couple['cast']).explode('cast') # создаем DataFrame, в колонке которого содержаться пары
couple.cast.value_counts() #считаем кол-во повторов


# ВАРИАНТ 2

# In[525]:


# решение аналогично первому варинту
df = data[['original_title','cast']].copy() 
df.cast = df.cast.str.split('|')
actors = df.cast
couple=actors.apply(combinations_couple).reset_index() #ф-ия combinations_couple в предоработке
couple.columns = ['movie_index', 'cast']
couple=couple.assign(cast=couple['cast']).explode('cast')
couple.cast.value_counts()


# # Submission

# In[526]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[527]:


# и убедиться что ни чего не пропустил)
len(answers)

