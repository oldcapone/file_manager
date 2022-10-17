from functions import avtor, dirs, files, add_separators
import os
from my_chet import start

def test_avtor():
    assert avtor() == "Игорь Иванов"

#Тестирование получения папок в текущей директории
def test_dirs():
    assert dirs() == [d for d in os.listdir() if os.path.isdir(os.path.join(d))]

#Тестирование получения файлов в директории
def test_files():
    assert files() == [d for d in os.listdir() if os.path.isfile(os.path.join(d))]


#Не понятно как проверять сложные функцие которые требуют ввод данных
# def  test_my_chet():
#     assert start() histoty = []
