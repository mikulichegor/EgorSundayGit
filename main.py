import math
def delenie():
    a = int(input('Введите первое число:'))
    b = int(input('Введите первое число:'))
    print(f'Ответ:{a / b}')

def sinus():
    x = int(input("Введите значение угла: "))
    print(math.sin(x))



def cosinus():
    num_1 = int(input('Введите число для косинуса: '))
    print(f'Результат: {math.cos(num_1)}')

def pluskakashki():
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
        pluskakashki()
    elif answer =='-':
        pass

    elif answer =='/':
        delenie()
    elif answer =='**':

    elif answer == '*':
        pass

        pass
    elif answer == '**':
        pass
    elif answer == '%':
        pass
    elif answer =='sin':
        sinus()
    elif answer == '//':
      pass
    elif answer == 'cos':
        cosinus()





menu()
