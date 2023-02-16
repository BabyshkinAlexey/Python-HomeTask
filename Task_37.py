def revert(n):
    if n == 0:
        return ""
    k = int(input("Введите эллемент: "))
    return revert(n-1) + " " + str(k)

size = int(input("Введите число: "))
print(revert(size))