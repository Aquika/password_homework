app = input('Введите пароль:')

p = len(app)
ap = 1
q = 'b'
try:
    result = ap / p
    res = int(app)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю соблюдены')


    




   

