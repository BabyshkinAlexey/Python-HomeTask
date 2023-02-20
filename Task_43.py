list_n = list(map(int, input().split()))
count = 0
for i in range(len(list_n) - 1):
    if list_n[i] is None:
        continue
    count_i = 1
    flag = True
    for j in range(i + 1, len(list_n)):
        if list_n[j] is not None and list_n[i] == list_n[j]:
            count_i += 1
            list_n[j] = None 
    count += count_i // 2
print(count)
        
        