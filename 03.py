# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

n = 4
i = 1
my_dict = {}
summ = 0
while i <= n:
    m = round((1 + 1 / i) ** i, 2)
    summ = summ + m
    my_dict[i] = m
    i =i+1


print(my_dict, 'sum= ', summ )
