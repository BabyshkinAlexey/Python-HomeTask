n = int(input("Введите число: "))

def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)
    
print(f"f({n}) = {f(n)}")