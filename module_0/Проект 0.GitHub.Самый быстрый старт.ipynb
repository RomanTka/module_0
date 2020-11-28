{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Угадай число"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Исходный код"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 254,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Загадано число от 1 до 100\n",
      "50\n",
      "Угадываемое число меньше 50 \n",
      "25\n",
      "Угадываемое число больше 25 \n",
      "37\n",
      "Угадываемое число меньше 37 \n",
      "32\n",
      "Угадываемое число меньше 32 \n",
      "29\n",
      "Угадываемое число больше 29 \n",
      "31\n",
      "Угадываемое число меньше 31 \n",
      "30\n",
      "Вы угадали число 30 за 7 попыток.\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "count = 0                            # счетчик попыток\n",
    "number = np.random.randint(1,101)    # загадали число\n",
    "print (\"Загадано число от 1 до 100\")\n",
    "\n",
    "while True:                        # бесконечный цикл\n",
    "    predict = int(input())         # предполагаемое число\n",
    "    count += 1                     # плюсуем попытку\n",
    "    if number == predict: break    # выход из цикла, если угадали\n",
    "    elif number > predict: print (f\"Угадываемое число больше {predict} \")\n",
    "    elif number < predict: print (f\"Угадываемое число меньше {predict} \")\n",
    "        \n",
    "print (f\"Вы угадали число {number} за {count} попыток.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 255,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Загадано число от 1 до 100\n",
      "Вы угадали число 86 за 86 попыток.\n"
     ]
    }
   ],
   "source": [
    "number = np.random.randint(1,101)    # загадали число\n",
    "print (\"Загадано число от 1 до 100\")\n",
    "for count in range(1,101):         # более компактный вариант счетчика\n",
    "    if number == count: break    # выход из цикла, если угадали      \n",
    "print (f\"Вы угадали число {number} за {count} попыток.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 256,
   "metadata": {},
   "outputs": [],
   "source": [
    "def game_core_v1(number):\n",
    "    '''Просто угадываем на random, никак не используя информацию о больше или меньше.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 0\n",
    "    while True:\n",
    "        count+=1\n",
    "        predict = np.random.randint(1,101) # предполагаемое число\n",
    "        if number == predict: \n",
    "            return(count) # выход из цикла, если угадали\n",
    "        \n",
    "        \n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=(1000))\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 257,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 101 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "101"
      ]
     },
     "execution_count": 257,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# запускаем\n",
    "score_game(game_core_v1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 258,
   "metadata": {},
   "outputs": [],
   "source": [
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = np.random.randint(1,101)\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict: \n",
    "            predict += 1\n",
    "        elif number < predict: \n",
    "            predict -= 1\n",
    "    return(count) # выход из цикла, если угадали"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 259,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 33 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 259,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Проверяем\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Доработанный код"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 260,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randrange\n",
    "def game_core_v3(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, \n",
    "        больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 0\n",
    "    if number >= 50: #сокращаем поиск до 50 чисел\n",
    "        count += 1\n",
    "        if number < 75: #сокращаем поиск до 25 чисел  [50,75)\n",
    "                count += 1\n",
    "                predict = np.random.randint(50,75)\n",
    "                while number != predict:\n",
    "                    count += 1\n",
    "                    if number > predict:\n",
    "                        predict += 1\n",
    "                    elif number < predict: \n",
    "                        predict -= 1\n",
    "        else: #сокращаем поиск до 25 чисел  [75,100]\n",
    "                count += 1\n",
    "                predict = np.random.randint(75,101)\n",
    "                while number != predict:\n",
    "                    count += 1\n",
    "                    if number > predict:\n",
    "                        predict += 1\n",
    "                    elif number < predict: \n",
    "                        predict -= 1\n",
    "    else:\n",
    "        count += 1\n",
    "        if  number > 25:#сокращаем поиск до 25 чисел  (25,50)\n",
    "            count += 1\n",
    "            predict = np.random.randint(26,50)\n",
    "            while number != predict:\n",
    "                count += 1\n",
    "                if number > predict:\n",
    "                    predict += 1\n",
    "                elif number < predict: \n",
    "                    predict -= 1\n",
    "        else: #сокращаем поиск до 25 чисел  [1,25]\n",
    "            count += 1\n",
    "            predict = np.random.randint(1,26)\n",
    "            while number != predict:\n",
    "                count += 1\n",
    "                if number > predict:\n",
    "                    predict += 1\n",
    "                elif number < predict: \n",
    "                    predict -= 1\n",
    "    return(count) # выход из цикла, если угадали\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 261,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 10 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 261,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Проверяем\n",
    "score_game(game_core_v3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 262,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randrange\n",
    "def number_seacrh(number, predict):\n",
    "    '''Получаем на вход угадываемое число и произвольно полученное число. Уменьшаем или увеличиваем его в зависимости от того, \n",
    "        больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count=0\n",
    "    while number != predict:\n",
    "        count += 1\n",
    "        if number > predict:\n",
    "            predict += 1\n",
    "        elif number < predict: \n",
    "            predict -= 1\n",
    "    return(count)\n",
    "\n",
    "\n",
    "def game_core_v4(number):\n",
    "    '''Сначала сокращаем диапозон поиска числа до 25 чисел (при этом сравнение считается как попытка),\n",
    "        устанавливаем любое random число в полученном диапозоне, а потом используем функцию number_search.\n",
    "        Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 0\n",
    "    if number >= 50: #сокращаем поиск до 50 чисел\n",
    "        count += 1\n",
    "        if number < 75: #сокращаем поиск до 25 чисел  [50,75)\n",
    "            count += 1\n",
    "            predict = np.random.randint(50,75)\n",
    "            count += number_seacrh(number,predict)\n",
    "        else: #сокращаем поиск до 25 чисел  [75,100]\n",
    "            count += 1\n",
    "            predict = np.random.randint(75,101)\n",
    "            count += number_seacrh(number,predict)\n",
    "    else:\n",
    "        count += 1\n",
    "        if  number > 25:#сокращаем поиск до 25 чисел  (25,50)\n",
    "            count += 1\n",
    "            predict = np.random.randint(26,50)\n",
    "            count += number_seacrh(number,predict)\n",
    "        else: #сокращаем поиск до 25 чисел  [1,25]\n",
    "            count += 1\n",
    "            predict = np.random.randint(1,26)\n",
    "            count += number_seacrh(number,predict)\n",
    "    return(count) # выход если угадали\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 263,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 10 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 263,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Проверяем\n",
    "score_game(game_core_v4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 264,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randrange\n",
    "def number_seacrh(number, predict):\n",
    "    '''Получаем на вход угадываемое число и произвольно полученное число. Уменьшаем или увеличиваем его в зависимости от того, \n",
    "        больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count=0\n",
    "    while number != predict:\n",
    "        count += 1\n",
    "        if number > predict:\n",
    "            predict += 1\n",
    "        elif number < predict: \n",
    "            predict -= 1\n",
    "    return(count)\n",
    "\n",
    "\n",
    "def game_core_v5(number):\n",
    "    '''Сначала сокращаем диапозон поиска числа до 12-13 чисел (при этом сравнение считается как попытка),\n",
    "        устанавливаем любое random число в полученном диапозоне, а потом используем функцию number_search.\n",
    "        Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 0\n",
    "    if number > 50: #сокращаем поиск до 50 чисел\n",
    "        count += 1\n",
    "        if number < 75: #сокращаем поиск до 25 чисел  (50,75]\n",
    "            count += 1\n",
    "            if number < 63:#сокращаем поиск до 12 чисел  (50,62]\n",
    "                count += 1\n",
    "                predict = np.random.randint(51,63)\n",
    "                count += number_seacrh(number,predict)\n",
    "            else:#сокращаем поиск до 13 чисел  [63,75]\n",
    "                count += 1\n",
    "                predict = np.random.randint(63,76)\n",
    "                count += number_seacrh(number,predict)\n",
    "        else: #сокращаем поиск до 25 чисел  (75,100]\n",
    "            count += 1\n",
    "            if number < 88:#сокращаем поиск до 12 чисел  (75,87]\n",
    "                count += 1\n",
    "                predict = np.random.randint(76,88)\n",
    "                count += number_seacrh(number,predict)\n",
    "            else:\n",
    "                count += 1#сокращаем поиск до 13 чисел  [88,100]\n",
    "                predict = np.random.randint(88,101)\n",
    "                count += number_seacrh(number,predict)\n",
    "    else:\n",
    "        count += 1\n",
    "        if  number > 25:#сокращаем поиск до 25 чисел  (25,50]\n",
    "            count += 1\n",
    "            if number > 37:#сокращаем поиск до 12 чисел  (37,50]\n",
    "                count += 1\n",
    "                predict = np.random.randint(38,51)\n",
    "                count += number_seacrh(number,predict)\n",
    "            else:#сокращаем поиск до 12 чисел  [26,37]\n",
    "                count += 1\n",
    "                predict = np.random.randint(26,38)\n",
    "                count += number_seacrh(number,predict)\n",
    "        else: #сокращаем поиск до 25 чисел  [1,25)\n",
    "            count += 1\n",
    "            if number > 12:#сокращаем поиск до 12 чисел  (12,25]\n",
    "                count += 1\n",
    "                predict = np.random.randint(13,26)\n",
    "                count += number_seacrh(number,predict)\n",
    "            else:#сокращаем поиск до 12 чисел  [1,12]\n",
    "                count += 1\n",
    "                predict = np.random.randint(1,13)\n",
    "                count += number_seacrh(number,predict)\n",
    "    return(count) # выход если угадали"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 7 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 265,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Проверяем\n",
    "score_game(game_core_v5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
   "metadata": {},
   "outputs": [],
   "source": [
    "def game_core_v6(number):\n",
    "    '''Доработали сокращения диапозона до 12 чисел и добавили условие проверки равенства'''\n",
    "    count = 0\n",
    "    first = 1 #первое число диапозона поиска\n",
    "    last = 100 #последнее число диапозона поиска\n",
    "    middle = 0 #середина числового отрезка (точнее целая её целая часть)\n",
    "    while last-first > 11:#   \n",
    "        middle = (first+last)//2\n",
    "        count += 1\n",
    "        if number > middle:\n",
    "            first = middle\n",
    "        elif number == middle:\n",
    "            first = middle\n",
    "            last = middle + 1\n",
    "            break\n",
    "        else:\n",
    "            last = middle  \n",
    "    predict = np.random.randint(first,last)\n",
    "    count += number_seacrh(number,predict)\n",
    "    return(count) # выход если угадали"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 267,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 5 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 267,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Проверяем\n",
    "score_game(game_core_v6)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
