# 팩토리얼(factorial) 구하기(1) : 1 ~ n까지의 곱을 구하기
def fact(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

print(fact(10))


# 팩토리얼 구하기(2) : 재귀호출 이용

def fact2(n):
    if n <= 1:  # 종료조건
        return 1
    return n * fact2(n-1) #더작은 입력값

print(fact2(10))

# n * (n-1) * (n-1-1) * (n-1-1-1) * ....
# 재귀 호출에는 종료조건이 반드시 필요하다.
# 종료 조건이 없으면 재귀에러(RecursionError)나 스택오버플로(stack overflow)등 문제 발생.