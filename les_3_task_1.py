# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MAX_NUMBER = 99
MIN_DIV = 2
MAX_DIV = 9

print('Делитель    Чисел на него делится')

for div in range(MIN_DIV, MAX_DIV + 1):
    print(f'{div:>6} {MAX_NUMBER // div:>16}')


# Вариант 2
# result = {}
# for n in range(2, 10):
#    result[n] = []
#    for f in range(2, 100):
#        if f % n == 0:
#            result[n].append(f)
#    print(f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.')