# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
N = int(input("Введите длину списка: "))


list = []
for i in range (N):
    list.append(random.randint(0,20))
print(list)

M = 0
if (N % 2 != 0):
    M = int(N//2)

list1 = []
for i in range (N//2):
    list1.append(list[i]*list[N-1-i])
if (M > 0):
    list1.append(list[M]*list[M]) 
print(list1)




    
