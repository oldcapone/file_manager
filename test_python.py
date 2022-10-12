from functions import func_max, func_min, func_sum_list, map_subtraction_list_t, math_pi_t
import math
import pytest


numbers = [-5, -3, 0, 1, 2, 3, 4, 5, 7, 8, 10, 11]

# Проверка списока чисел больше 3
def test_filter_max3():
    assert list(filter(func_max, numbers)) == [3, 4, 5, 7, 8, 10, 11]


# Проверка списока чисел меньше 3
def test_filter_min3():
    assert list(filter(func_min, numbers)) == [-5, -3, 1, 2]

# Проверка сложения списков

def test_map_sum():
    assert list(map(func_sum_list, (2, 4, 5), (1, 2, 3))) == [3, 6, 8]

# Проверка вычитания списков
def test_map_subtraction():
    assert list(map(map_subtraction_list_t, (2, 4, 5), (1, 2, 3))) == [1, 2, 2]

l1=[1, 4, 5, 2, 456, 12]
def test_sorted():
    assert sorted(l1) == [1, 2, 4, 5, 12, 456]

def test_sort():
    assert sorted(['e', 'h', 'l', 'l', 'o'], reverse = True ) == ['o', 'l', 'l', 'h', 'e']

def test_math_pi():
    assert math_pi_t(2, 10) == 16.283185307179586

def test_math_pi_2():
    assert math.pi == 3.141592653589793

def test_math_sqrt():
    assert math.sqrt(4) == 2
def test_math_sqrt_2():
    assert math.sqrt(9) == 3

def test_math_pow():
    assert math.pow(3,2) == 9
def test_math_pow():
    assert math.pow(3,3) == 27
  
#math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).

def test_math_hypot():
    assert math.hypot(3,4) == 5.0
def test_math_hypot_2():
    assert math.hypot(6,5) == 7.810249675906654