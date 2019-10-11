import random

letters = tuple('qwertyuiopasdfghjklzxcvbnm')
big = tuple([i.upper() for i in letters])
symbols = tuple('!@#$%^&*()_')
numbers = tuple('1234567890')

pass_list = tuple()
choice = input('Использовать ли маленькие буквы в пароле? (y/n): ')
if choice == 'y':
    pass_list += letters
    choice = input('Использовать ли большие буквы в пароле? (y/n): ')
    if choice == 'y':
        pass_list += big
        choice = input('Использовать ли цифры в пароле? (y/n): ')
        if choice == 'y':
            pass_list += numbers
            choice = input('Использовать ли символы? (y/n): ')
            if choice == 'y':
                pass_list += symbols

length = input('Какова длинна пароля?: ')
count = input('Сколько паролей создать вам для выбора?: ')
password = ''
result = {}

for i in range(int(count)):
    for _ in range(int(length)):
        password += random.choice(pass_list)
    result[i] = password
    password = ''

for key in result:
    print(str(key) + ')' + (result[key]))

input('Чтобы продолжить нажмите Enter')
