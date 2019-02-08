import turtle  # turtle 이라는 파일을 추가한다.

# 주의점!!: 가져올 파일과 내가 만든 파일하고 이름이 같으면 안 된다.

turtle.shape("turtle")  # 거북이를 그린다

turtle.forward(100)  # 거북이가 보는 방향으로 이동한다
turtle.lt(120)  # 거북이가 왼쪽으로 회전한다
turtle.forward(100)

# 문제 1) 거북이로 삼각형을 그려보세요.
turtle.lt(120)
turtle.forward(100)


# 문제 2) 거북이로 사각형을 그려보세요.
turtle.lt(30)
turtle.forward(100)
turtle.lt(90)
turtle.forward(100)
turtle.lt(90)
turtle.forward(100)

# 문제 3) 거북이로 집을 그려보세요.

# 문제 4) 거북이로 별을 그려보세요.
turtle.forward(200)
turtle.lt(90)
turtle.forward(25)
turtle.lt(142)
turtle.forward(50)
turtle.lt(142)
turtle.forward(50)
turtle.lt(142)
turtle.forward(50)
turtle.lt(142)
turtle.forward(50)
turtle.lt(146)
turtle.forward(50)

# ======= 위에서 식을 만들자 ! =======
turtle.exitonclick()  # 클릭할 때까지 종료를 막는다
