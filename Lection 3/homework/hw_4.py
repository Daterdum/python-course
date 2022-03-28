# Реализуйте хеш-таблицу на основе списка.
# Хешировать будем только целые числа.
# Хеш-функция (_hash()) должна возвращать индекс элемента в списке. Пример ниже
# Выбор способа хеширования оставляю за вами, можно придумать свой, можно подглядеть в интернете
# Необходимо реализовать методы add, get, delete и print, позволяющий вывести список в удобном виде
# На первом этапе можно игнорировать коллизии и увеличение storage, необходимо подобрать функцию
# и размер storage (в идеале придумать способо разрещения таких случаев)
# такие, чтобы полученные индексы не выходили за размер storage
# Список не должен менять размер свой размер в процессе использования кроме **

# * Реализуйте разрешение коллизий любым методом на ваш выбор
# ** Реализуйте автоматическое увеличение bucket-ов при заполнении половины существующих

# Пример:
# При инициализации таблицы создаем пустой storage из десяти бакетов:
# [None, None, None, None, None, None, None, None, None, None]
# Пусть функция хеширования выглядит как:
#
# def hash(self, value):
#     return value // 5 + 3
#
# Тогда при попытке положить элемент 30 в таблицу мы положим его в ячейку с индексом 30 // 5 + 3 = 9
# Наш storage будет выглядеть теперь так:
# [None, None, None, None, None, None, None, None, None, 30]
#
# P.S. Во всех заранее созданных методах класса обращаться к storage можно через self.storage
import random
import typing as t

INITIAL_SIZE = 10 ** 3
MULTIPLIER = 4


class HashTable:
    def __init__(self):
        # Create buckets for our Table with None in each bucket
        self.storage = [None] * INITIAL_SIZE

    def add(self, value) -> t.Optional[int]:
        # Add value to storage, return index/hash on success, None on failure
        pass

    def find(self, value) -> int:
        # Find value in storage and return its index
        pass

    def delete(self, value) -> bool:
        # Delete value from storage, return True on success, return False on failure
        pass

    def _hash(self, value) -> int:
        # Based on value return index of element
        pass

    def print(self):
        # Print all buckets
        pass


if __name__ == '__main__':
    hash_table = HashTable()
    for _ in range(INITIAL_SIZE // MULTIPLIER):
        hash_table.add(random.choice(range(INITIAL_SIZE * MULTIPLIER)))
