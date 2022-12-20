#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def Fact(num):
    list = []
    result = 1
    i = 1
    while i <= num:
        result = result * i
        i=i+1
        list.append(result)
    return list

n = int(input ('Введите число: '))
print(Fact(n))