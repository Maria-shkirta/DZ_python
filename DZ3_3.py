# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a=[1.1, 1.2, 3.1, 5, 10.01]

b=[round(a[i]%1,3) for i in range(len(a))]
print(b)

c=max(b)-min(b)
print(c)