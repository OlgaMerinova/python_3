# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

# Пример:

# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
N = int(input("Введите длину списка: "))


list = []
for i in range (N):
    list.append('%.2f' % random.random())
print((list))


# smallest_numer = min(list)
# bigger_number = max(list)

print(max(list)-min(list))


