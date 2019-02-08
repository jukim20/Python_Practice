# 문제)  가로세로를 직접 입력받고 사각형 삼각형의 넓이를 구해보세요

width = int(input("가로를 입력하세요 >>> "))
length = int(input("세로를 입력하세요 >>> "))

print("사각형의 넓이는 ", width * length, "이다.")
print("삼각형의 넓이는 ", width * length / 2, "이다.")

# 문제) 숫자를 입력받고 5의 배수이면서 3의 배수인지체크해보세요

num = int(input("숫자를 입력하세요 >>> "))

if num % 3 == 0 and num % 5 == 0:
    print("True")
else:
    print("False")

# 문제)  주민번호를 입력받고  나이 출력 , 생일 출력

ssn = input("주민번호를 입력하세요 (- 포함) >>> ")

if len(ssn) != 14:
    print("잘못 입력했습니다.")
elif ssn[7] != "1" and ssn[7] != "2" and ssn[7] != "3" and ssn[7] != "4":
    print("잘못 입력했습니다.")
else:
    if ssn[7] == "1" or ssn[7] == "2":
        year = "19" + ssn[0:2]
    else:
        year = "20" + ssn[0:2]
    age = 2018 - int(year) + 1
    if age > 0:
        print("나이: ", age, "세")
    else:
        print("잘못 입력했습니다.")

    birth_month = ssn[2:4]
    birth_day = ssn[4:6]
    print("생일: " + birth_month + "월 " + birth_day + "일")


# 문제) 주민번호를 입력받고 성년, 미성년 출력 (1999) 기준
    if age >= 20:
        print("성년입니다.")
    else:
        print("미성년입니다.")

#  문제 2) 10~20까지 숫자를 출력해보자
num = 10

while num <= 20:
    print(num)
    num += 1

#  문제 1)  0~9 까지 출력 하는데
#   1) 짝수만 출력

num = 0
while num < 10:
    if num % 2 == 0:
        print(num)
    num += 1

#   2) 5보다 큰수만 출력

num = 0
while num < 10:
    if num > 5:
        print(num)
    num += 1