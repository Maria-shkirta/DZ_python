# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

N=int(input('Введите число N: '))

posl=[round((1+1/i)**i,2) for i in range(1,N+1)]
print(posl)

summ=sum(posl)
print(summ)