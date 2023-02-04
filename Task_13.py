n = int(input("Введите количество дней: "))
count = 0
maxi = 0
for i in range(n):
    x = int(input("Введите температуру: "))
    if x > 0:
        count += 1
    else:
        if maxi < count:
            maxi = count
        count = 0
print(maxi)