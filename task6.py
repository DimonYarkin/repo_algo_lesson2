"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random


def guess_the_number(number_attempts=0, nuber1=0):
    if nuber1 == 0:
        nuber1 = int(random.random() * 100)
    if number_attempts == 10:
        return f'Было загаданно число: {nuber1}'
    try:
        user_number = int(input('Введите ваше число от 0 до 100: '))
    except ValueError:
        print('Введено не число повторите ввод: ')
        return guess_the_number(number_attempts, nuber1)
    if user_number == nuber1:
        return 'Поздравляем вы угадали!!!'
    elif user_number > nuber1:
        print('Вы ввели число больше чем загаданное')
        return guess_the_number(number_attempts + 1, nuber1)
    elif user_number < nuber1:
        print('Вы ввели число меньше чем загаданное')
        return guess_the_number(number_attempts + 1, nuber1)


if __name__ == '__main__':
    print(guess_the_number())
