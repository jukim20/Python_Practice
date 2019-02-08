lst = [1, 3, 54, 23, 5, 67, 7, 3, 4]
# i = 0
# j = i + 1
for i in range(len(lst)):
    for j in range(len(lst) - 1):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print(lst)  # [67, 54, 23, 7, 5, 4, 3, 3, 1]

