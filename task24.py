# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

from random import randint

count_bush = int(input('Введите кол-во кустов: '))
sum_collection = 0
max_sum = 0

data_1 = list()
for i in range(count_bush):
    data_1.append(randint(0, 10))

for i in range(len(data_1)-2):
    sum_collection = data_1[i]+data_1[i+1]+data_1[i+2]
    if sum_collection > max_sum:
        max_sum = sum_collection
        bush_1 = i + 1
        bush_2 = i + 2
        bush_3 = i + 3
print(f'количество ягод на каждом кусте:{data_1}')
print()
print(f'номера кустов: {bush_1}+{bush_2}+{bush_3}={sum_collection}')