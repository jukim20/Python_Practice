# 문제 1) 사각형의 넓이를 구해보세요  (가로 10, 세로 3)

width = 10
length = 3

print("사각형의 넓이 >>> ", width * length)  # 문자와 숫자를 같이 출력할 때는 구분자로 , (쉼표) 를 사용한다

# 응용문제 1) 위 가로 세로를 이용해서 삼각형의 넓이를 구해보세요

print("삼각형의 넓이 >>> ", width * length / 2)


# 응용문제 2) 가로세로를 직접 입력받고 사각형 삼각형의 넓이를 구해보세요
width = input("가로를 입력하세요 >>> ")
length = input("세로를 입력하세요 >>> ")

print("사각형의 넓이 >>> ", int(width)*int(length))  # 문자로 들어와있기 때문에 숫자로 바꿔줘야됨
print("삼각형의 넓이 >>> ", int(width)*int(length)/2)

# 응용문제 3) 월급을 입력받고 연봉을 구해보세요 (세금 10% 제외)
# 예) 출력 ==> 월급 ==> 20, 연봉에서 10% 제외한 금액

salary = int(input("월급을 입력하세요 >>> "))  # 입력 받는 순간 숫자로 들어오기 때문에 아래서 변환x
print("월급 >>> ", salary, "만원,", "연봉 >>>", salary * 12 * 0.9, "만원")

# print("연봉 = ", int(salary) * 12 * 0.9)