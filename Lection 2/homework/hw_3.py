# На входе последовательность из десяти чисел, выведите максимально возможную сумму трех из этих чисел
import random

MAX_NUM = 100000

def get_max_sum_of_three(numbers: tuple):
    # insert your code here


if __name__ == '__main__':
    numbers = tuple(random.randint(0, MAX_NUM) for _ in range(10))
    print(numbers)
    get_max_sum_of_three(numbers)
