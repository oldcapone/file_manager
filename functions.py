import pytest
import math
import os

# Функция декоратор
# f - исходная фукнция
def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('*' * 20)
        result = f(*args, **kwargs)
        print(result)
        # поведение после вызова
        print('*' * 20)
        return result

    # возвращается функция inner с новым поведением
    return inner

#Функции файлового менеджера
@add_separators
def avtor():
    fio = "Игорь Иванов"
    return fio
#Просмотр файлов в директории
# генератор списка
# [элемент <цикл for> if <условие>]
def files():
    files = [d for d in os.listdir() if os.path.isfile(os.path.join(d))]
    return files

#Просмотр папок в директории
def dirs():
    dirs = [d for d in os.listdir() if os.path.isdir(os.path.join(d))]
    return dirs

#Функция фильтрует все числа более 3

def func_max(x):
    if x >=3:
        return x

#Функция фильтрует все числа меньше 3
def func_min(x):
    if x < 3:
        return x
#Функция складывает списки

def func_sum_list(a, b):
    return a + b
# Функция вычитания списков

def map_subtraction_list_t(d, e):
    return d - e
def math_pi_t(a,b):
    return math.pi*a+b


