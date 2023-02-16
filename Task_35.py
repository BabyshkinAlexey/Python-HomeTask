n = int(input("Введите число: "))

def is_simple_num(n):
    n = abs(n)
    if n < 2:
        return "NO"
    for i in range(2,n):
        if n % i == 0:
            return "NO"
    return "YES"

print(is_simple_num(n))