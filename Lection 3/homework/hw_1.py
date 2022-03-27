# Отсортируйте список случайной длины в зависимости от мода (reverse) по возрастанию или по убыванию
import random

MAX_NUM = 10**5


def sort(tpl: tuple, reverse: bool = False):
    lst = list(tpl)
    # insert your code here
    return lst


if __name__ == '__main__':
    numbers = tuple(random.randint(0, MAX_NUM) for _ in range(random.randint(0, MAX_NUM)))
    print(sort(
        numbers,
        reverse=True  # change mod here
    ))
