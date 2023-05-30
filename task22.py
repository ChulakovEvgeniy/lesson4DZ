# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint

count_1 = int(input('Введите кол-во элементов в масcиве: '))
count_2 = int(input('Введите кол-во элементов в масcиве: '))

data_1 = list()
for i in range(count_1):
    data_1.append(randint(0, 10))

data_2 = list()
for i in range(count_1):
    data_2.append(randint(0, 10))


print(data_1)
print()
print(data_2)
print(sorted(set(data_1).intersection(set(data_2))))