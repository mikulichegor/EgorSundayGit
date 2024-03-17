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
        pass
    elif answer =='cos':
        pass

menu()

