#  문제는 각자 레벨에 맞춰서 골라서 푸세요~
#  if 문제 ) 숫자 하나를 입력받고 "짝수" , "홀수" 출력
num = int(input("숫자를 입력하세요 >>> "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

print("========================================")

#  반복문 문제 ) 0~10 중에서 홀수 만 출력
num = 0
while num <= 10:
    if num % 2 == 1:
        print(num)
    num += 1

print("========================================")

#  문제 ) 0~10중에서 전부 더한값 출력
sum = 0
num = 0

while num <= 10:
    sum += num
    num = 0
print("합 : ", sum)

num1 = int(input("숫자 1을 입력하세요 >>> "))
num2 = int(input("숫자 2를 입력하세요 >>> "))

print("========================================")

#  문제 ) 숫자 2개를 입력받고 사이의 정수를 출력
num1 = int(input("숫자 1을 입력하세요 >>> "))
num2 = int(input("숫자 2를 입력하세요 >>> "))

if num1 < num2:
    while num1 < num2:
        print(num1+1)
        num1 += 1
elif num1 > num2:
    while num1 > num2:
        print(num2+1)
        num2 += 1

print("========================================")

lst = [-9, 0, 10, 2005, -6, 21, 100]

# 리스트 문제 ) 위의 리스트 안의 각요소의 총합을 출력
num = 0
total = 0
print(len(lst))  # 리스트 안의 요소의 개수
while num < len(lst):
    total += lst[num]
    num += 1
print(total)
# 문제 ) 위의 리스트  양수갯수 출력 , 음수 갯수 출력 , 짝수갯수 출력
num = 0
positive = 0
while num < len(lst):
    if lst[num] > 0:
        positive += 1
    num += 1
print(positive)
lst = [-9, 0, 10, 2005, -6, 21, 100]
# 문제 ) 값을 입력받고 인덱스를 출력 ==> 예) 0 ==> 1 ,  -6 ==> 4
# 문제 ) 위 리스트 안에서 가장 큰값을 출력 예) 2005
max = lst[0]

