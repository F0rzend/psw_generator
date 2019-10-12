import random
import string

from PyInquirer import prompt
from examples import custom_style_1, custom_style_2, custom_style_3


def psw_type():
    questions = [
        {
            'type': 'checkbox',
            'message': 'Использовать в пароле',
            'name': 'types',
            'choices': [
                {
                    'name': 'Маленькие буквы',
                    'checked': True
                },
                {
                    'name': 'Заглавные буквы',
                    'checked': True
                },
                {
                    'name': 'Цифры',
                    'checked': True
                },
                {
                    'name': 'Символы'
                },

            ],
        }
    ]
    types = prompt(questions, style=custom_style_2)
    psw_list = tuple()
    if 'Маленькие буквы' in types['types']:
        psw_list += tuple(string.ascii_lowercase)

    if 'Заглавные буквы' in types['types']:
        psw_list += tuple(string.ascii_uppercase)

    if 'Цифры' in types['types']:
        psw_list += tuple(string.digits)

    if 'Символы' in types['types']:
        psw_list += tuple(string.punctuation)

    if not psw_list:
        return psw_type()

    print()
    return psw_list


def length():
    questions = [
        {
            'type': 'input',
            'name': 'length',
            'message': 'Какой длинны будет пароль?',
            'default': '12',
        },
    ]
    length = prompt(questions, style=custom_style_1)
    if not length['length']:
        return length()
    else:
        return int(length['length'])


def count():
    questions = [
        {
            'type': 'input',
            'name': 'count',
            'message': 'Сколько паролей создать вам для выбора?',
            'default': '8',
        }
    ]
    count = prompt(questions, style=custom_style_1)
    if not count['count']:
        return count()
    else:
        return int(count['count'])


def generate(psw_list, length, count):
    result = []
    psw = ''
    for i in range(count):
        for _ in range(length):
            psw += random.choice(psw_list)
        result.append(psw)
        psw = ''

    return result


def save_psw(passwords_list):
    print(passwords_list)
    questions = [
        {
            'type': 'list',
            'name': 'psw',
            'message': 'Какой пароль вы хотели бы использовать?',
            'choices': passwords_list
        }
    ]

    choice = prompt(questions, style=custom_style_3)
    questions = [
        {
            'type': 'input',
            'name': 'comment',
            'message': f'Пожалуйста добавьте комментарий к паролю {choice["psw"]}'
        }
    ]
    comment = prompt(questions, style=custom_style_1)
    with open('passwords.txt', 'a') as f:
        f.write(f'{choice["psw"]} - {comment["comment"]}')


if __name__ == '__main__':
    save_psw(generate(psw_type(), length(), count()))
