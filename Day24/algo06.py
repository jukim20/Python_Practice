# 최대공약수 구하기

def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)