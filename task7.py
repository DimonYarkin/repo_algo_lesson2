"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def my_rec(num_user, summ_left=0, summ_n=1):
    print(summ_left)
    if summ_left == summ_n:
        return f'Равенство выполнелось {summ_left == summ_n}'
    elif summ_left < summ_n:
        return my_rec(num_user, summ_left + 1, num_user * (num_user + 1) / 2)


if __name__ == '__main__':
    try:
        num = int(input('Введите число: '))
        print(my_rec(num))
    except ValueError:
        print('Введено не число')
