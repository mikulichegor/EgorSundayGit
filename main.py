
import math

def cosinus():
    num_1 = int(input('Введите число для косинуса: '))
    print(f'Результат: {math.cos(num_1)}')



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
    elif answer == '*':
        pass
    elif answer == '/':
        pass
    elif answer == '**':
        pass
    elif answer == '%':
        pass
    elif answer == '//':
        pass

    elif answer == 'sin':
        pass
    elif answer == 'cos':
        cosinus()





menu()



