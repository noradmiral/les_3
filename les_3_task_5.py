# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
# Если таких элементов несколько, то вывожу любой из них.


import random


SIZE = 10
MIN_ITEM = -20
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Массив:', array, sep='\n')

max_negative_num = 0

for i, item in enumerate(array):

    if item < 0 and max_negative_num == 0:
        max_negative_num = item
        num_index = i

    elif max_negative_num < item < 0:
        max_negative_num = item
        num_index = i

if max_negative_num == 0:
    print('Отрицательных элементов не найдено.')

else:
    print(f'Максимальный отрицательный элемент: {max_negative_num}\nЕго индекс: {num_index}')



# Вариант 2
# import random
#
# r = [random.randint(-99, 99) for _ in range(100)]
# print(f'Массив: {r}')
#
# min_index = 0
#
# for i in r:
#     if r[min_index] > i:
#         min_index = r.index(i)
#
# if r[min_index] >= 0:
#     print(f'В массиве нет отрицательных элементов')
# else:
#     print(f'В массиве минимальный отрицательный элемент: {r[min_index]}.',
#             f'Находится в массиве на позиции {min_index}')