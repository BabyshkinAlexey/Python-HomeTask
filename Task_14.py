# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число: "))
i = 1
print("Степени 2-ки до числа", n, ":")
while i <= n:
    i *= 2
    if i > n : break
    else: print(i, end=" / ")