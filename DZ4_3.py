# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst=list(map(int,input('Введите числа через пробел: ').split()))

print(lst)

lst_two=[]
[lst_two.append(i) for i in lst if i not in lst_two]

print(lst_two) 