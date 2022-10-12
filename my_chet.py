def start():
    chet = 0
    name = "НЕТ"
    histoty = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'на счету {chet}')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            plus = float(input("Введите сумму на сколько пополнить счет: "))
            chet +=plus
            print(chet)
        elif choice == '2':
            buy = float(input("Введите сумму покупки: "))
            if buy>chet:
                print("Денег не хватает")
            else:
                chet-=buy
                name = (input("Введите название покупки: "))
                histoty.append((name , buy))
        elif choice == '3':
            print(histoty)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')


