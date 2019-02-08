# 최대값 최소값 구하기
def find_max(a):
    n = len(a)
    max = a[0]
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
    return max

lst = [10, 9, 49, 38, 4, 182, 51, 93, 1]
print(find_max())

# 최대값 위치구하기
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

print(find_max_idx(lst))