
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
    elif answer == '-':
        num1 = int(input('введите 1 число:'))
        num2 = int(input('введите 2 число:'))
        print(f'ответ: {num1 - num2}')
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
        pass


menu()
