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
        a = input('Введите первое число:')
        b = input('Введите второре число:')
        return f'Ответ: {a+b}'
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
        sinus()
    elif answer =='cos':
        pass

menu()


def sinus():
    x = int(input("Введите значение угла: "))
    print(math.sin(x))
