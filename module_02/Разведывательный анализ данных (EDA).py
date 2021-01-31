#!/usr/bin/env python
# coding: utf-8

# In[825]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
stud_math_v0 = pd.read_csv('stud_math.csv')


# ### Предобработка

# In[826]:


# функция для нахождения и вывода информации о кол-во пустых строк в столбце
def nan_cell_print(col):
    n = len(stud_math[col])-(stud_math[col].value_counts()).sum()
    if n > 0:
        return print('Столбец {0} содержит {1} незаполненных значений с типом nan.'.format(col, n))
    else:
        return print('Столбец {0} полностью заполнен.'.format(col))


# функция для определения вывода информаиии о уникальных значениях
def info_uniq_nan(col):
    arr = stud_math[col].unique()
    uniq_list = []
    for i in arr:
        i = str(i)
        if str(i) != 'nan':
            uniq_list.append(i)
    uniq_list.sort()
    return print('В колонке {2} количество уникальных значений {0} - {1}.'.format(len(uniq_list), ((',').join(uniq_list)), col))


# функция для построение гистограммы распределения и определения признака для числовых переменных
def hist(col, x):
    IQR = stud_math[col].quantile(0.75) - stud_math[col].quantile(0.25)
    Q1 = stud_math[col].quantile(0.25)
    Q3 = stud_math[col].quantile(0.75)
    print('25-й перцентиль: {},'.format(Q1), '75-й перцентиль: {},'.format(Q3),
          "IQR: {}, ".format(IQR), "Границы выбросов: [{f}, {l}].".format(f=Q1 - 1.5*IQR, l=Q3 + 1.5*IQR))
    return stud_math[col].loc[stud_math[col].between(Q1 - 1.5*IQR, Q3 + 1.5*IQR)].hist(bins=x, label='IQR'), plt.legend()


# функция для построение построения боксплотов номинативных нечисловых переменных
def get_boxplot(col):
    fig, ax = plt.subplots(figsize=(14, 4))
    sns.boxplot(x=col, y='score',
                data=stud_math.loc[stud_math.loc[:, col].isin(
                    stud_math.loc[:, col].value_counts().index[:10])],
                ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + col)
    plt.show()


# тест Стьюдента
def get_stat_dif(column):
    cols = stud_math.loc[:, column].value_counts().index[:10]
    combinations_all = list(combinations(cols, 2))
    for comb in combinations_all:
        if ttest_ind(stud_math.loc[stud_math.loc[:, column] == comb[0], 'score'],
                     stud_math.loc[stud_math.loc[:, column] == comb[1], 'score']).pvalue \
                <= 0.05/len(combinations_all):  # Учли поправку Бонферони
            print('Найдены статистически значимые различия для колонки', column)
            break


# ### 1. Выполним первичную обработку данных

# In[827]:


display(stud_math_v0.head(5))  # получим инф-ию по имеющимся данным
stud_math_v0.info()


# В столбце score есть незаполенные значения, т.к. целевой параметр для анализа - это оценка учеников, то удалим строки содержащие NaN в столбце score. Количество строк сократиться на 6 штук.  

# In[828]:


stud_math = stud_math_v0.dropna(subset=['score'])
stud_math = stud_math.reset_index()
stud_math.drop(['index'], inplace=True, axis=1)
display(stud_math.head(5))
stud_math.info()


# In[829]:


for i in stud_math.columns:
    nan_cell_print(i)


# Итак, имеем 30 колонок из которых заполнены полностью только 4, включая целевой показатель. 

# ### 2. Начнем анализ данных с числовых переменных. 

# ### 2.1 age - количественная переменная 

# In[830]:


nan_cell_print('age')
stud_math.age.hist(bins=8, label='Все значения')
hist('age', 7)


# Выбросов данных нет, хоть ученики страше 21 и выходят за правую границу выбросов. Данные полностью находятся в исследуемом  диапозоне от 15 до 22 лет.

# In[831]:


stud_math.failures.value_counts()


# ### 2.2 Medu - номинативная числовая переменная 

# In[832]:


nan_cell_print('Medu')
stud_math.Medu.hist(bins=5, label='Все значения')
hist('Medu', 5)
info_uniq_nan('Medu')


# Выбросов данных нет, данные полностью находятся в рассматриваемом диапозоне от 0 до 4 с шагом 1.

# ### 2.3 Fedu - номинативная числовая переменная 

# In[833]:


nan_cell_print('Fedu')
stud_math.Fedu.hist(bins=40, label='Все значения')
hist('Fedu', 3)
info_uniq_nan('Fedu')


# Видим явный выброс, ему соответствует уникальное значение 40. Предполагая, что в данных опечатка - вместо 40 должна была бать категория 4. Два решения, либо избавиться от значения либо заменить его на 4. Выбираю второе. 

# In[834]:


stud_math.Fedu.loc[stud_math['Fedu'] == 40] = 4.0
nan_cell_print('Fedu')
stud_math.Fedu.hist(bins=4, label='Все значения')
info_uniq_nan('Fedu')


# Выбросов данных нет, данные полностью находятся в рассматриваемом диапозоне от 0 до 4 с шагом 1.

# ### 2.4 traveltime - номинативная числовая переменная 

# In[835]:


nan_cell_print('traveltime')
stud_math.traveltime.hist(bins=4, label='Все значения')
hist('traveltime', 3)
info_uniq_nan('traveltime')


# Выбросов данных нет, данные полностью находятся в рассматриваемом диапозоне от 1 до 4 с шагом 1.

# ### 2.5 studytime - номинативная числовая переменная 

# In[836]:


nan_cell_print('studytime')
stud_math.studytime.hist(bins=4, label='Все значения')
hist('studytime', 3)
info_uniq_nan('studytime')


# Выбросов данных нет, данные полностью находятся в рассматриваемом диапозоне от 1 до 4 с шагом 1.

# ### 2.6 studytime, granular - номинативная числовая переменная 

# In[837]:


nan_cell_print('studytime, granular')
stud_math['studytime, granular'].hist(bins=4, label='Все значения')
hist('studytime, granular', 3)
info_uniq_nan('studytime, granular')


# Гистограмма "studytime, granular" "Все значение" по форме напоминает гистограмму "studytime", только симметрично отображенную.

# In[838]:


stud_math.plot(x='studytime, granular',
               y='studytime',
               kind='scatter',
               grid=True,)


# Видим, что значения "studytime, granular" получены путем умножения значений "studytime" на -3. Отсюда делаем вывод, что столбец "studytime, granular" прямопропорционален столбцу "studytime", а следовательно дополнительной информативной нагрузки за собой не несет. Поэтому удалеем его. 

# In[839]:


stud_math = stud_math.drop('studytime, granular', 1)


# ### 2.7 failures  - номинативная числовая переменная 

# In[840]:


nan_cell_print('failures')
stud_math.failures.hist(bins=4, label='Все значения')
hist('failures', 4)
info_uniq_nan('failures')


# Выбросов нет т.к. значение 1,2,3,0. Не совсем понимаю смысл сбора данных в данную колонку таким образом. Т.к. данный столбец посути номинативно - количественный, ведь мы знаем точное число неудач у некоторых учеников (1,2 или 3). Но при этом других учеников с "0" в ячейке просто относим в другую группу, которая опять же не информатинва, потому что одновременно содержит 2 группы учеников: одни с n=0, другие с n > 3 неудач. Проще было либо собирать кол-во неудач у каждого, либо делить на группы с определенным интервалом. 

# ### 2.8 famrel - номинативная числовая переменная 

# In[841]:


nan_cell_print('famrel')
stud_math.famrel.hist(bins=4, label='Все значения')
hist('famrel', 3)
info_uniq_nan('famrel')


# Есть явный выбросы: -1.0 и 0, т.к. данные должны содержать значения от 1 до 5 c шагом 1. Полагаю, что те, кто поставил 0 и -1 хотели таким образом количественно оценить проблемы в семье. Но тем менее они попадают в номинативную категорию 1 - очень плохо. Поэтому заменим значения с -1  и  0 на 1. 

# In[842]:


stud_math.famrel.loc[stud_math['famrel'] < 1] = 1
nan_cell_print('famrel')
stud_math.famrel.hist(bins=5, label='Все значения')
info_uniq_nan('famrel')


# ### 2.9 freetime - номинативная числовая переменная 

# In[843]:


nan_cell_print('freetime')
stud_math.freetime.hist(bins=5, label='Все значения')
hist('freetime', 4)
info_uniq_nan('freetime')


# Выбросов данных нет, данные полностью находятся в рассматриваемом диапозоне от 1 до 5 с шагом 1.

# ### 2.10 goout - номинативная числовая переменная 

# In[844]:


nan_cell_print('goout')
stud_math.goout.hist(bins=5, label='Все значения')
hist('goout', 5)
info_uniq_nan('goout')


# Выбросов данных нет, данные полностью находятся в рассматриваемом диапозоне от 1 до 5 с шагом 1.

# ### 2.11 health - номинативная числовая переменная 

# In[845]:


nan_cell_print('health')
stud_math.health.hist(bins=5, label='Все значения')
hist('health', 5)
info_uniq_nan('health')


# Выбросов данных нет, данные полностью находятся в рассматриваемом диапозоне от 1 до 5 с шагом 1.

# ### 2.12 absences - количественная  переменная 

# In[846]:


nan_cell_print('absences')
stud_math.absences.hist(bins=20, label='Все значения')
hist('absences', 3)


# Присутствуют явные выбросы, один из учеников отсутствовал более календарного года, другой более учебного. Отфильтруем данные.

# In[847]:


stud_math = stud_math.loc[stud_math['absences'] <= 20]
nan_cell_print('absences')
stud_math.absences.hist(bins=10, label='Все значения')


# ### 2.13 score - количественная переменная (целевая переменная)

# In[848]:


nan_cell_print('score')
stud_math.score.hist(bins=7, label='Все значения')
hist('score', 7)


# ### 3. Корреляционный анализ

# Для количественных переменных

# In[849]:


stud_math[['age', 'absences', 'score']].corr()


# Для числовых переменных

# In[850]:


stud_math.corr()


# Со score все числовые переменные имеют слабую корреляцию (точнее все имееют очень слабую корреляцию < 0,3, кроме  failures который, имеет просто слабую корреляцию [0.3;0.5]). Так же среди других показателей в матрице можно заметить, что образования родителей средне коррелированы друг с другом. Относительно целевого показателя score можно заметить, что с взрослением оценка уменьшается, так же как и при увеличении время проведенного с друзьями. Увеличение оценки слабо коррелирует с образованием матери, ещё слебее с образованием отца. Внешкольные занятия учебой так же имеют положительную корреляцию с оценкой, примерно равную коррелиции образование отца с оценкой. 

# ### 4. Анализ номинативных переменных 

# In[851]:


nom_col = stud_math.select_dtypes(include='object').columns


# In[852]:


for col in nom_col:
    nan_cell_print(col)
    info_uniq_nan(col)


# In[853]:


for col in nom_col:
    get_boxplot(col)


# По графикам кажется, что влияют следующие параметры: sex, address, Mjob, schoolsup, internet, romantic, activities, higher, higher

# Проверим, есть ли статистическая разница в распределении оценок по номинативным признакам, с помощью теста Стьюдента. Проверим нулевую гипотезу о том, что распределения оценок по различным параметрам неразличимы:

# In[854]:


for col in nom_col:
    get_stat_dif(col)


# ### 4. Вывод

# In[855]:


for i in stud_math.columns:
    nan_cell_print(i)


# В данных много пустых значений, изначально было заполнено 3 колонки (school, sex, age). После обработки полностью заполненными стали 5 колонок (school, sex, age, absences, score).   

# Были найдены выбросы в следующих 3 колонках  Fedu, famrel, absences. Замечу, что колонки  Fedu, famrel - номинативные числовые колонки, соотвественно с ними проводить математические операции бессмысленно, ибо они не обозначают количество, а делят на группы. И в обоих колонках были опечатки. В Fedu вместо 4 было указано 40, в famrel были значения 0 и -1, которые мы отнесли к группе очень плохо, т.е. заменили на 1. Колонка absences является количественной, поэтому выбросы посчитали арифметически, исходя из значений в колонке, и отфильтровали их. 

# Выводы из корреляицонного анализа написанны выше. Замечу в анализе не было столбца "studytime,granular", т.к. я исключил его на этапе обработки. Т.к. он полностью коррелирует со "studytime " за исключением направленности. 

# В модель передаем следующие колонки. С комментарием присмотреться к Fedu по причине корреляции с Medu. А так же к failures  см. п.2.7 (я бы его вообще исключил). 

# In[856]:


stud_math_model = stud_math.loc[:, ['school', 'sex', 'address', 'Mjob', 'Fjob',
                                    'schoolsup', 'paid', 'higher', 'internet', 'romantic', 'age',
                                    'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout',
                                    'health', 'absences', 'score']]
stud_math_model

