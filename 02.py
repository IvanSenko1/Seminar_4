# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from re import I


num = int(input("Введите N "))
Spisok = []
i = 2

while i <= num:
    if num % i == 0:
        Spisok.append(i)
        num //= i
    else:
        i += 1

print(Spisok) 