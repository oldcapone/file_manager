import pytest
import math

#Функции файлового менеджера
def avtor():
    fio = "Игорь Иванов"
    return fio




#Функции для тестирования менеджера
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