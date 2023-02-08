arr = [1, 2, 3, 4, 5]
print("Начальный массив: ")
print(arr)
k = 3
size = len(arr)
new_arr = []
for i in range (k, size):
    new_arr.append(arr[i])
for j in range (k):
    new_arr.append(arr[j])

print("Измененный массив: ")
print(new_arr)