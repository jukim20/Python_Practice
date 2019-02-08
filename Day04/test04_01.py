# 문제 ) 산술연산자를 사용해보세요 (10 , 3)

print(10 + 3)

# 문제 ) 숫자 2개를 입력받고  산술연산을 출력 하세요
# 10 + 2 = 12

num1 = int(input("숫자1을 입력하세요 >>> "))
num2 = int(input("숫자2를 입력하세요 >>> "))

print(num1 + num2)

# 문제 ) 월급을 입력받고 연봉을 구해보세요 (세금 10% 제외)
# 예) 출력 ==> 월급 ==> 20 , 연봉 에서 10% 제외한금액 (???)

salary = int(input("월급을 입력하세요 >>> "))
print("월급 = ", salary, "만원, ", "연봉 = ", salary * 12 * 0.9, "만원")

#  응용문제 1) 숫자하나를 입력받고 양수인지 음수 , 0 인지 출력 해보세요

num = int(input("숫자를 입력하세요 >>> "))
if num > 0:
    print("이 숫자는 양수입니다.")
if num < 0:
    print("이 숫자는 음수입니다.")
if num == 0:
    print("이 숫자는 0 입니다.")

if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("0")


#  응용문제 2) 성적 (0~100 ) 하나 입력받고 60이 넘으면 합격 이하면 불합격 출력

grade = int(input("성적을 입력하세요 >>> "))
if grade >= 60:
    if grade < 100:
        print("합격")
    else:
        print("잘못 입력하였습니다.")


if grade < 60:
    if grade < 0:
        print("잘못 입력하였습니다.")
    else:
        print("불합격")
