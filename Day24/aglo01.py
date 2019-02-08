# 1부터 n까지 구하기
def sum_n(n):
    tot = 0
    for i in range(1, n+1):
        tot += i
    return tot

print(sum_n(10))

def sum_n2(n):
    return n * (n + 1) // 2

print(sum_n2(10))