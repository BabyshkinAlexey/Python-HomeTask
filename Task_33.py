n = int(input("Введите кол-во оценок: "))
arr = [0] * n

for i in range(n):
    arr[i] = int(input("Введите оценку: "))
    
maxi = max(arr)
mini = min(arr)

for i in range(n):
    if arr[i] == maxi:
        arr[i] = mini

print(arr)