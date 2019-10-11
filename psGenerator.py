import random
import string


pass_list = tuple()
choice = input('Использовать ли маленькие буквы в пароле? (y/n): ')
if choice == 'y':
    pass_list += tuple(string.ascii_lowercase)
choice = input('Использовать ли большие буквы в пароле? (y/n): ')
if choice == 'y':
    pass_list += tuple(string.ascii_uppercase)
choice = input('Использовать ли цифры в пароле? (y/n): ')
if choice == 'y':
    pass_list += tuple(string.digits)
choice = input('Использовать ли символы? (y/n): ')
if choice == 'y':
    pass_list += tuple(string.punctuation)

length = input('Какова длинна пароля?: ')
count = input('Сколько паролей создать вам для выбора?: ')
password = ''
result = {}

for i in range(1, int(count) + 1):
    for _ in range(int(length)):
        password += random.choice(pass_list)
    result[i] = password
    password = ''

for key in result:
    print(str(key) + ')' + (result[key]))
