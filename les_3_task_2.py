# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив:', array, sep='\n')

even_ind = []

for i, item in enumerate(array):

    if item % 2 == 0:
        even_ind.append(i)

print('Четные числа находятся на позициях:', even_ind, sep='\n')



# Вариант 2
# import random

# r = [random.randint(0, 99) for _ in range(10)]
# print(f'Первый массив {r}')
# index_even = []
# for n in r:
#    if n % 2 == 0:
#        index_even.append(r.index(n))
# print(f'Индексы чётных элементов первого массива: {index_even}')