# 동명이인 찾기

def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["여정", "병욱", "정수", "제원선생님", "여정"]
print(find_same_name(name))

