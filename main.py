def plus():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print(a + b)

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
        pass
    elif answer =='*':
        pass
    elif answer =='/':
        pass
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

