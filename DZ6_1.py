
# Задача 1. Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b=list(filter(lambda x:x<5,a))
# print(b)

# Задача 2. Возвести в квадрат список.
# a=[2,3,7]
# b=list(map(lambda x:x**2,a))
# print(b)

# Задача 3. Создать список из четных чисел от 1 до 10.
# a=[i for i in range(1,10) if i%2==0]
# print(a)

# Задача 4. Пронумеровать список.
# a=['Berlin','Lisbon','London']
# b=enumerate(a)
# print(list(b))

#Задача 5. Объединить список номеров и имен сотрудников в массив кортежей.
# a=['Andrew','Ben','Bill']
# b=[56,2,47]
# c=zip(b,a)
# print(list(c))
