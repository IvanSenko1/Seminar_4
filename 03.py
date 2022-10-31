# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import numbers
from unittest import result


numbers = [3, 5, 3, 6, 7, 18, 53]
result = []
for i in numbers:
    if numbers.count(i) < 2:
        result.append(i)
print(result)