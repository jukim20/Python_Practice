a = 10
b = 20

print(a == b)

if True:
    print("실행문1")

if False:
    print("실행문2")

if a == b:
    print("a는 b와 같다")

if a != b:
    print("a는 b와 다르다")

# 응용문제 1) 숫자하나를 입력받고 양수인지 음수, 0 인지 출력해보세요

num = int(input("숫자를 입력하세요 >>> "))
if num > 0:
    print("이 숫자는 양수입니다")
if num < 0:
    print("이 숫자는 음수입니다")
if num == 0:
    print("이 숫자는 0 입니다")

# 응용문제 2) 성적 (0~100) 하나 입력받고 60이 넘으면 합격, 이하면 불합격 출격
# 성적을 입력하세요 >>> 60 ==> 합격 , 59 ==> 불합격, (-10, 101) ==> 잘못 입력했습니다

grade = int(input("성적을 입력하세요 >>> "))


if grade >= 60:
    if grade > 100:
        print("잘못 입력했습니다")
    if grade < 100:
        print("합격")

if grade < 60:
    if grade < 0:
        print("잘못 입력했습니다")
    if grade > 0:
        print("불합격")


