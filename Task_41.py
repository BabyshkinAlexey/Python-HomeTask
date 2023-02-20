size = int(input("Введите количество эллементов массива: "))
arr = [0] * size

for i in range(size):
    print(f"Ведите {i + 1} эллемент массива: ", end = "")
    arr[i] = int(input())


count = 0
for i in range(1, size - 1):
    if arr[i - 1] < arr[i] > arr[i + 1]:
        count += 1

print(count)