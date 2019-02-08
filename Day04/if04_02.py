# 문제 1) 양수 음수 0 을 구분하는 식을 만들어보세요.

num = int(input("숫자를 입력하세요 >>> "))
if num > 0:
    print("양수입니다.")
elif num < 0:
    print("음수입니다.")
else:
    print("0입니다.")

# 문제 2) 짝수 홀수를 구분하는 식을 만들어보세요.

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 문제 3) 숫자 2개를 입력받고 ??가 ??보다 크다 or 작다 출력
num1 = int(input("숫자 1를 입력하세요 >>> "))
num2 = int(input("숫자 2를 입력하세요 >>> "))

if num1 > num2:
    print("숫자 1은 숫자 2보다 크다.")
elif num1 < num2:
    print("숫자 1은 숫자 2보다 작다.")
else:
    print("숫자 1은 숫자 2와 같다.")

