# 1. 출력
# 2. 인자 1
# 3. 인자 2


def show_line():
    print("==============")


def show_num(num):
    print(num)


def show_even(num):
    if num % 2 == 0:
        print("짝수")


def add_all(num):
    total = 0
    for i in range(num):
        total += i
    print("총 합: ", total)


def add(num1, num2):
    print(num1 + num2)


def add_range(num1, num2):
    if num2 < num1:
        temp = num2
        num2 = num1
        num1 = temp
    while num1 < num2:
        num1 += 1

# 문제 1) 정수를 인자로 사용해서 정수 숫자만큼 "="*20 을 그려주는 함수
# 문제 2) 정수와 문자를 인자로 사용해서 "문자"*20 을 그려주는 함수


def multiply(num):
    for i in range(num):
        print("=" * 20)


multiply(2)


def my_multiply(num, str1):
    for i in range(num):
        print(str1 * 20)


my_multiply(3, "%")
my_multiply(2, "i")
