# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

b=input('Введите вещественное число: ')

x=[int(a) for a in str(b)]
print(x)

summ=sum(x)
print(summ)
