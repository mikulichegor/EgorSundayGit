def delenie():
    a = int(input('Введите первое число:'))
    b = int(input('Введите первое число:'))
    print(f'Ответ:{a / b}')




def menu():
    answer = input('Выберите действие:\n'
                   '+ - сложение\n'
                   '- - вычитание\n'
                   '* - умножение\n'
                   '/ - деление\n'
                   '** - возведение в степень\n'
                   '% - остаток от деления\n'
                   '// - целочисленное деление\n'
                   'sin - синус\n'
                   'cos - косинус:')
    if answer == '+':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второре число:'))
        print(f'Ответ: {a + b}')
    elif answer =='-':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второре число:'))
        print(f'Ответ: {a - b}')
    elif answer =='*':
        pass
    elif answer =='/':
        delenie()
    elif answer =='**':
        pass
    elif answer =='%':
        pass
    elif answer =='//':
        pass
    elif answer =='sin':
        pass
    elif answer =='cos':
        pass

menu()

