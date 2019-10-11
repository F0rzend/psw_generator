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

confirm = None
while confirm != 'y':
    while choice not in range(1, int(count) + 1):
        choice = int(input('Введите номер пароля, который вы бы хотели использовать: '))
    confirm = input(f'Вы собираетесь использовать пароль "{result[choice]}"? (y/n): ')


comment = input('Пожалуйста добавьте комментарий к паролю: ')

with open('passwords.txt', 'a') as f:
    f.write(f'{result[choice]} - {comment}\n')

with open('passwords.txt', 'r') as f:
    print(f.read())
