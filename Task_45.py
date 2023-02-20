k = int(input("Введите число К: "))
my_list = []
for i in range(k):
    sum_i = 0
    for j in range(1, i//2+1):
        if i % j == 0:
            sum_i += j
    my_list.append((i, sum_i))
    
for i in range(len(my_list) - 1):
    for j in range(i + 1 , len(my_list)):
        if my_list[i][0] == my_list[j][1] and my_list[j][0] == my_list[i][1]:
            print(*my_list[i])