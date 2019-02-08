import turtle

# 과제

# 응용문제 1) 10 , 3 을 변수에 저장후 10 + 3 = 13 (서식문자사용) 출력
num1 = 10
num2 = 3

print(num1+num2)

# 응용문제 : 숫자 2개를 입력받고  산술연산을 출력 하세요
# 10 + 2 = 12
num1 = int(input("숫자 1을 입력하세요 >>> "))
num2 = int(input("숫자 2를 입력하세요 >>> "))

print("숫자 1 + 숫자 2 = ", num1 + num2)

# 문제 1) 거북이로 삼각형을 그려보세요
turtle.shape("turtle")
turtle.forward(100)
turtle.lt(120)
turtle.forward(100)
turtle.lt(120)
turtle.forward(100)


# 문제 2) 거북이로 사각형을 그려보세요
# 문제 3) 거북이로 집을 그려보세요
# 문제 4) 거북이로 별을 그려보세요

turtle.exitonclick()