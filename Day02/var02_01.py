"""
* 변수 ( variable ) : 데이터를 담을 수 있는 공간

* 변수의 특징 :
    1) 이름은 숫자로 시작할 수 없다.
    2) 특수문자는 _ (언더바)를 사용할 수 있다.
    3) 보통은 영어 소문자로 이름을 짓는다.
    4) 값을 한가지만 저장가능하다 ==> 새로운 값이 들어오면 기존 값은 사라진다.

* 사용법 ==> 이름 = 값
    1) 산술연산
    2) 대입연산 ==>  a = b  ==>  b의 값을 a에 복사 (저장)한다.
"""

# 10을 출력하고 싶을 때
print(10)

# 변수를 사용할 경우 :
num = 10
print(num)  # 10

# 새로운 값이 들어오면 기존 값은 사라진다 의 예:

num = 1
num = -10
num = 100
num = 0
num = 1000
num = -30

print(num)  # -30

# 응용문제 : 10 , 3 을 변수에 저장 후 %d + %d = %d (서식문자 사용) 출력
num1 = 10
num2 = 3
print("더하기 : %d + %d = %d" % (num1, num2, num1+num2))

# 응용문제 2 : 위의 식을 , 를 사용해서 출력
print("더하기 : ", num1, "+", num2, "=", num1+num2)
