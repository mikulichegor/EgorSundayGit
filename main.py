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
        plus()
    elif answer =='-':
        minus()
    elif answer =='*':
        multiple()
    elif answer =='/':
        divide()
    elif answer =='**':
        stepen()
    elif answer =='%':
        percent()
    elif answer =='//':
        fullch()
    elif answer =='sin':
        pass
    elif answer =='cos':
        pass

def minus():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второре число:'))
    print(f'Ответ: {a - b}')

def plus():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второре число:'))
    print(f'Ответ: {a + b}')

def multiple():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второре число:'))
    print(f'Ответ: {a * b}')

def divide():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второре число:'))
    print(f'Ответ: {a / b}')

def stepen():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второре число:'))
    print(f'Ответ: {a ** b}')

def percent():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второре число:'))
    print(f'Ответ: {a % b}')

def fullch():
    a = int(input('Введите первое число:'))
    b = int(input('Введите второре число:'))
    print(f'Ответ: {a // b}')



menu()

