n = int(input("Введите кол-во арбузов: "))
maxi = 0
mini = 9999
for i in range(n):
    m = int(input("Введите вес арбуза: "))
    if m > maxi:
        maxi = m
    if m < mini:
        mini = m
print("Минимальныфй вес: ", mini,"/ максимальный вес: ", maxi)