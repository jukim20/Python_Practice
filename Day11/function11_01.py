# 함수 (function)
"""
일정한 기능을 하는 프로그래밍 조각
자주 사용하는 코드를 반복해서 작성하지 않도록 하기 위해서 사용한다.

1. 내장함수 ( print(), input() ...)
2. 사용자 정의 함수 ==> show_line1() ==> 직접 만들어서 사용한다.

# 직접 만들기 위해서는 설계도를 먼저 작성해야한다. (함수의 정의)
    # 함수 정의하는 법 ==> def + 함수이름 + () : + 둘여쓰기 (실행문)
    # 정의된 함수를 이용하는 법 ==> 함수이름 + ()

"""


def show_line1():
    print("===========================")


def show_line2():
    print("!==========================")
    print("!==========================")


show_line1()
show_line2()
print("ㅇㅇㅇ")


def show_pow(num):  # 제곱을 구해주는 함수  # 함수의 매개변수는 num 이다.
    print(num * num)


show_pow(3)  # 인자 : 3  ==> 3을 인자라고 한다. 함수의 인자는 3이다.
show_pow(5)

# 문제 1) 정수를 인자로 사용해서 정수 숫자만큼 라인을 그려주는 함수를 만들자.


def show_lines(num):
    for i in range(num):
        print("================")


show_lines(3)

# 문제 2) 정수를 인자로 사용해서 정수가 짝수 홀수 음수 양수를 구별하는 함수


def show_sign(num):
    if num % 2 == 0:
        print("짝수")
    else:
        print("홀수")
    if num < 0:
        print("음수")
    elif num > 0:
        print("양수")
    else:
        print("0")


show_sign(10)


# 문제 3) 정수 2개를 인자로 사용해서 + - * / % 의 결과를 알려주는 함수


def cal(num1, num2):
    print("합 : ", num1 + num2)
    print("차 : ", num1 - num2)
    print("곱 : ", num1 * num2)
    print("분 : ", num1 / num2)
    print("몫 : ",  num1 % num2)


cal(10, 3)

# 문제 4) 정수를 1개 인자로 사용해서 0~ 그 정수까지 다 더한 합을 알려주는 함수


def add_all(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    print("총 합 : ", sum)


add_all(3)

# 문제 5) 정수 2개를 인자로 사용해서 정수 사이의 합을 더해주는 함수


def add_between(num1, num2):
    if num2 < num1:
        temp = num2
        num2 = num1
        num1 = temp
    total = 0
    while num1 < num2 +1:
        total += num1
        num1 += 1
    print(total)


"""
def add_between(num1, num2):
    if num1 < num2:
        sum = 0
        i = num1
        while i < num2 + 1:
            sum += i
            i += 1
        print(sum)
    elif num1 > num2:
        sum = 0
        i = num2
        while i < num1 + 1:
            sum += i
            i += 1
        print(sum)
    else:
        print(0)
"""

add_between(1, 5)
add_between(5, 1)

