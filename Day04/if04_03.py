# 논리 연산자  ==> 조건을 한번에 여러개 비교할 때 사용한다.

"""
and  ==>  a and b   : a 와 b 가 둘 다 참이면 참
or   ==>  a or b    : a 가 참이거나 b 가 참이면 참
not  ==>  not a     : a 가 거짓이면 참
"""

a = 10
b = 20
c = 60
d = 50

print(a < b and c > d)  # 둘 다 참이어야 결과가 참이 나옴

d = 70
print(a > b or c < d)  # 둘 중 하나만 참이여도 결과가 참이 나옴
print(not(a > b))  # 결과가 거짓이어야 참이 나옴
print(not (c > d))

print("=========================================================")

print(a < b and c > d)  # 둘 다 참이어야 결과가 참이 나옴

d = 30
print(a > b or c < d)  # 둘 중 하나만 참이여도 결과가 참이 나옴
a = 30
print(not(a > b))  # 결과가 거짓이어야 참이 나옴
print(not (c > d))

print("=========================================================")
num1 = int(input("성적을 입력해주세요 >>> "))
if num1 < 0 or num1 > 100:
    print("잘못입력했습니다")

# 90~99 면 A
elif num1 >= 90:
    print("합격: A")

elif num1 >= 85:
    print("합격: B")

elif num1 >= 73:
    print("합격: C")

else:
    print("불합격: F")

print("=========================================================")

# 문제 1) 아이디와 비밀번호를 입력받고 로그인을 해보세요.

db_id = "koreait"
db_pw = "12345"

id = input("아이디를 입력하세요 >>> ")
pw = input("비밀번호를 입력하세요 >>> ")

if id == db_id:
    if pw == db_pw:
        print("로그인 되었습니다.")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("없는 아이디입니다.")