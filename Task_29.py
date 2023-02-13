n = int(input("Введите число: "))
max_number = n
while n != 0:
    n = int(input("Введите число: "))
    if max_number < n:
        max_number = n
print(max_number)