import random
import string

pass_list = tuple()

choice = None
while choice != 'y' and choice != 'n':
    choice = input('Использовать ли маленькие буквы в пароле? (y/n): ')
    if choice == 'y':
        pass_list += tuple(string.ascii_lowercase)

choice = input('Использовать ли большие буквы в пароле? (y/n): ')
while choice != 'y' and choice != 'n':
    if choice == 'y':
        pass_list += tuple(string.ascii_uppercase)

choice = input('Использовать ли цифры в пароле? (y/n): ')
while choice != 'y' and choice != 'n':
    if choice == 'y':
        pass_list += tuple(string.digits)

choice = input('Использовать ли символы? (y/n): ')
while choice != 'y' and choice != 'n':
    if choice == 'y':
        pass_list += tuple(string.punctuation)

length = ''
while not length.isdigit():
    length = input('Какова длинна пароля?: ')

count = ''
while not count.isdigit():
    count = input('Сколько паролей создать вам для выбора?: ')


password = ''
result = {}

for i in range(int(count)):
    for _ in range(int(length)):
        password += random.choice(pass_list)
    result[i + 1] = password
    password = ''

for key in result:
    print(f'{key}) {result[key]}')
