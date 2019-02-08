print("10" + "10")  # 1010

# 이것을 막는 법: casting (형변환)

print(int("10") + int("10"))  # 20


num = input()
num2 = input()

# 응용문제 : 숫자 2개를 입력받고 산술연산을 출력하세요.
# 10 + 2 = 12

print("%d + %d = %d" % (int(num), int(num2), int(num) + int(num2)))
