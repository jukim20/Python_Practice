#   5) 0~9까지 전부 더한 합을 출력
#   6) 숫자를 2개 입력받고 그 사이의 정수를 출력 (3 , 7)  # 함정문제 (7 , 3)

count = 0
num = 0

while count < 10:
    num += count
    count += 1
print(num)

print("============================================================")

num1 = int(input("숫자 1을 입력하세요 >>> "))
num2 = int(input("숫자 2를 입력하세요 >>> "))

while num1 < num2 - 1:
    num1 += 1
    print(num1)

