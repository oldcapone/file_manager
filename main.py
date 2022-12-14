"""
. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию.
"""
import os
import shutil
import platform
import viktorina
import my_chet
import functions

name = "НЕТ"
histoty = []
while True:
    print('1. Создать папку;')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории)')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Cохранить содержимое рабочей директории в файл')
    print('0. Выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        dir = input("Введите название папки: ")
        os.mkdir(dir)
        print(f'Новая папка {dir} создана')
    # 2. удалить (файл/папку);
    elif choice == '2':
        del_dir = input("Введите название папки или файла для удаления: ")
        if os.path.isfile(del_dir) == True:
            os.remove(del_dir)
            print(f'Файл {del_dir} удален')
        elif os.path.exists(del_dir):
            shutil.rmtree(del_dir)
            print(f'Папка {del_dir} удалена')
        else:
            print(f'Папки или файла {del_dir} нет в директории')
    # 3 копировать(файл / папку);
    elif choice == '3':
        copy_dir = input("Введите название папки или файла который надо скопировать: ")
        new_dir = input("Введите новое название папки или файла: ")
        if os.path.isfile(copy_dir) == True:
            shutil.copy2(copy_dir, new_dir)
            print(f'Файл {copy_dir} скоприрован в {new_dir}')
        elif os.path.isfile(copy_dir) == False:
            shutil.copytree(copy_dir, new_dir)
            print(f'Папка {copy_dir} скоприрован в {new_dir}')
        else:
            print(f'Папки или файла {copy_dir} нет в директории')

        #4 просмотр содержимого рабочей директории;
    elif choice == '4':
        print(os.listdir())

        #5 посмотреть только папки
    elif choice == '5':
        print(functions.dirs())
        #6 посмотреть только файлы
    elif choice == '6':
        print(functions.files())
        # 7 просмотр информации об операционной системе
    elif choice == '7':
        print(platform.uname())
        #создатель программы;
    elif choice == '8':
        functions.avtor()
        # играть в викторину
    elif choice == '9':
        viktorina.get_person_and_question()
        # 10. мой банковский счет
    elif choice == '10':
        my_chet.start()
# Запись в файл сначала все файлы, потом все папки
    elif choice == '11':
        #Отрываем файл для записи
        with open('listdir.txt', 'w') as f:
            f.write(f'files: {functions.files()}\n')
            f.write(f'dir: {functions.dirs()}')
        # Отрываем файл для просмотра
        with open('listdir.txt', 'r') as f:
            # 1. Прочитать файл
            result = f.read()
            print(f'Содержимое файла\n',result)
    elif choice == '0':
        break
    else:
        print('Неверный пункт меню')
