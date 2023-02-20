# n = int(input("Введите кол-во эллементов 1-го массива: "))
# arr_n = [0] * n
# for i in range(n):
#     print(f"Введите {i + 1} эллемент массива: ", end = "")
#     arr_n[i] = int(input())
    
# m = int(input("Введите кол-во эллементов 2-го массива: "))
# arr_m = [0] * m
# for i in range(m):
#     print(f"Введите {i + 1} эллемент массива: ", end = "")
#     arr_m[i] = int(input())
    
# for i in range(n):
#     flag = False
#     for j in range(m):
#         if arr_n[i] == arr_m[i]:
#             flag = True
#             break
#     if not flag:
#         print(arr_n[i], end = "") 

n = int(input("Введите число n: "))
list1 =list(map(int, input().split()))
m = int(input("Введите число m: "))
list2 =list(map(int, input().split()))

s1 = set(list2)
for i in range(n):
    if list1[i] not in s1:
        print(list1[i], end = " ")