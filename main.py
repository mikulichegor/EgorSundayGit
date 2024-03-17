def powering(num_1,  num_2):
    num_1 = int(input('Введите число для возведения в стпень: '))
    num_2 = int(input('Введите число для возведения в стпень: '))
    print(f'Результат: {num_1**num_2}')

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
        print(f'Ответ: {a+b}')
    elif answer =='-':
        pass
    elif answer =='*':
        pass
    elif answer =='/':
        pass
    elif answer =='**':
        print(powering(num_1, num_2))
    elif answer =='%':
        pass
    elif answer =='//':
        pass
    elif answer =='sin':
        pass
    elif answer =='cos':
        pass



menu()

