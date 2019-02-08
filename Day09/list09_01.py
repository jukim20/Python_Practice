# 리스트 연산자

lst = [0] * 5
print(lst)

lst = ["안녕"] * 3
print(lst)

lst = ["안녕", "하이"] * 3
print(lst)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst1 + lst2)  # [1, 2, 3, 4, 5, 6]

lst3 = lst1 + lst2
print(lst3)  # [1, 2, 3, 4, 5, 6]


# 리스트 수정과 삭제
lst = [1, 2, 3]
lst[2] = 6
print(lst)

lst = [1, 2, 3, 4, 5]
lst[1] = ["aa", "bb", "cc"]
print(lst)  # 리스트 안에 리스트

lst[1:2] = ["aa", "bb", "cc"]
print(lst)  # [1, 'aa', 'bb', 'cc', 3, 4, 5]  # 그냥 리스트

