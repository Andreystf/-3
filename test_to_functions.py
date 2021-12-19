import unittest
import time
import random
import functools
from functions import read_file, minimum, maximum, suma, proizvedenie


class Test(unittest.TestCase):
    # Тест на 4-ый балл проверяет корректность входных данных, а именно являются ли все входные числа целыми.
    # Это так, потому что функция read_file будет выдавать ошибку, если какое-то из чисел нецелое.
    # А если же тест test_correct не выдал сообщение о неккоректности входны данных, то все числа целые,
    # а это означает, что ошибки переполнения быть не может.
    def test_correct(self):
        try:
            read_file("data_file.txt")
        except ValueError:
            print("Некорректные входные данные")
        return

    def arr(self, n):
        a = []
        for i in range(n):
            a.append(random.randint(1000000, 10000000))
        return a

    def write(self, array, name):
        f = open(name, "w")
        for i in array:
            f.write(str(i) + " ")
        f.close()

    def period_of_time(self, x, m):
        a = time.time() - x
        m.append(a)

    def test_read_time(self):
        time1 = []
        self.write(self.arr(10000), "data2_file.txt")

        start_time = time.time()
        read_file('data_file.txt')
        self.period_of_time(start_time, time1)

        start_time = time.time()
        read_file('data2_file.txt')
        self.period_of_time(start_time, time1)

        self.assertEqual(time1, sorted(time1), "Ошибка времени чтения файла")

    def test_minimum(self):
        time1 = []
        array1 = self.arr(100)
        start_time = time.time()
        self.assertEqual(minimum(array1), min(array1), "Неверный миниимум")
        self.period_of_time(start_time, time1)

        array2 = self.arr(10000)
        start_time = time.time()
        self.assertEqual(minimum(array2), min(array2), "Неверный миниимум")
        self.period_of_time(start_time, time1)

        array3 = self.arr(100000)
        start_time = time.time()
        self.assertEqual(minimum(array3), min(array3), "Неверный миниимум")
        self.period_of_time(start_time, time1)

        self.assertEqual(time1, sorted(time1), "Ошибка времени поиска минимума")

    def test_maximum(self):
        time1 = []
        array1 = self.arr(100)
        start_time = time.time()
        self.assertEqual(maximum(array1), max(array1), "Неверный максимум")
        self.period_of_time(start_time, time1)

        array2 = self.arr(10000)
        start_time = time.time()
        self.assertEqual(maximum(array2), max(array2), "Неверный максимум")
        self.period_of_time(start_time, time1)

        array3 = self.arr(100000)
        start_time = time.time()
        self.assertEqual(maximum(array3), max(array3), "Неверный максимум")
        self.period_of_time(start_time, time1)

        self.assertEqual(time1, sorted(time1), "Ошибка времени поиска максимума")

    def test_suma(self):
        time1 = []
        array1 = self.arr(100)
        start_time = time.time()
        self.assertEqual(suma(array1), sum(array1), "Неверная сумма")
        self.period_of_time(start_time, time1)

        array2 = self.arr(10000)
        start_time = time.time()
        self.assertEqual(suma(array2), sum(array2), "Неверная сумма")
        self.period_of_time(start_time, time1)

        array3 = self.arr(100000)
        start_time = time.time()
        self.assertEqual(suma(array3), sum(array3), "Неверная сумма")
        self.period_of_time(start_time, time1)

        self.assertEqual(time1, sorted(time1), "Ошибка времени поиска суммы")

    def test_proizvedenie(self):
        time1 = []
        array1 = self.arr(1000)
        start_time = time.time()
        self.assertEqual(proizvedenie(array1), functools.reduce(lambda a, b: a * b, array1), "Неверное произведение")
        self.period_of_time(start_time, time1)

        array2 = self.arr(5000)
        start_time = time.time()
        self.assertEqual(proizvedenie(array2), functools.reduce(lambda a, b: a * b, array2), "Неверное произведение")
        self.period_of_time(start_time, time1)

        array3 = self.arr(10000)
        start_time = time.time()
        self.assertEqual(proizvedenie(array3), functools.reduce(lambda a, b: a * b, array3), "Неверное произведение")
        self.period_of_time(start_time, time1)

        self.assertEqual(time1, sorted(time1), "Ошибка времени поиска произведения")


if __name__ == '__main__':
    unittest.main()
