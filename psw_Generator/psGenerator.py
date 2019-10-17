import random
import string
from functools import partial

from PyInquirer import prompt, Validator, ValidationError


class IntNumberValidator(Validator):
    def validate(self, document):
        if not document.text.isdigit():
            raise ValidationError(
                message='Введите число 1 - 100',
                cursor_position=len(document.text)
            )
        elif int(document.text) < 1:
            raise ValidationError(
                message='Введите число 1 - 100',
                cursor_position=len(document.text)
            )


def psw_type():
    questions = [
        {
            'type': 'checkbox',
            'qmark': '[?]',
            'message': 'Использовать в пароле',
            'name': 'symbols',
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
    types = prompt(questions)
    psw_list = ''
    if 'Маленькие буквы' in types['symbols']:
        psw_list += string.ascii_lowercase

    if 'Заглавные буквы' in types['symbols']:
        psw_list += string.ascii_uppercase

    if 'Цифры' in types['symbols']:
        psw_list += string.digits

    if 'Символы' in types['symbols']:
        psw_list += string.punctuation

    if not psw_list:
        print('Необходимо задействовать минимум один набор символов')
        return psw_type()

    print()
    return psw_list


def psw_length():
    questions = [
        {
            'type': 'input',
            'name': 'length',
            'message': 'Какой длинны будет пароль?',
            'default': '12',
            'validate': IntNumberValidator
        },
    ]

    length = prompt(questions)
    return int(length['length'])


def generate(symbols_list, pass_len, count=8):
    some_symbol = partial(random.choice, symbols_list)
    psw_list = [''.join([some_symbol() for _ in range(pass_len)]) for _ in range(count)]
    return psw_list


def save_psw(passwords_list):
    questions = [
        {
            'type': 'list',
            'name': 'psw',
            'message': 'Какой пароль вы хотели бы использовать?',
            'choices': passwords_list
        }
    ]

    choice = prompt(questions)
    questions = [
        {
            'type': 'input',
            'name': 'comment',
            'message': f'Пожалуйста добавьте комментарий к паролю {choice["psw"]}'
        }
    ]
    comment = prompt(questions)

    questions = [
        {
            'type': 'list',
            'name': 'confirm',
            'message': f'Пароль {choice["psw"]} будет сохранён в файле "passwords.txt"',
            'choices': [
                {
                    'name': 'YES'
                },
                {
                    'name': 'NO'
                },
            ]
        }
    ]
    confirm = prompt(questions)
    if confirm['confirm'] == 'YES':
        with open('passwords.txt', 'a') as f:
            f.write(f'{choice["psw"]} - {comment["comment"]}')
        print('Сохранено!')


def main():
    save_psw(generate(psw_type(), psw_length()))
    input('Нажмите Enter чтобы продолжить...')


if __name__ == '__main__':
    main()
