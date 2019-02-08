import time

start = time.time()
#  print(start)  # 1521680307.1369152

num = 0
while num < 1000000:
    num += 1

end = time.time()
print("소요시간 >>> ", end - start)

print("=========================================================")
# 타자 연습게임 -->
# 리스트 안의 단어가 하나씩 순서대로 보여지고  # 똑같이 맞추면 point += 1  # 걸린 시간 출력
lst = ["python", "Java", "Jsp", "C", "Cpp", "C#"]

i = 0
point = 0

input("시작을 원하시면 아무 키나 눌러주세요 >>> ")
start = time.time()
while i < 6:
    print(lst[i])
    word = input("단어를 받아쓰세요 >>> ")
    if word == lst[i]:
        point += 1
    i += 1
end = time.time()

print("점수 : ", point, "점")
print("소요시간 : %.2f " % (end - start), "초")

# 문제는 각자 레벨에 맞춰서 골라서 푸세요
# if 문제 ) 숫자 하나를 입력받고 "짝수", "홀수" 출력

num = int(input("숫자를 입력하세요 >>> "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 심화문제 : 단어를 섞어보세요 ==> 섞는 방법: 랜덤으로 하나를 선택, 첫번째와 교환 (100번 반복)
# 랜덤으로 하면 중복 항목이 있을 수 있으니 섞을 수 밖에 없다.

# 반복문 문제 ) 0~10 중에서 홀수만 출력
num = 0
while num < 10:
    if num % 2 == 1:
        print(num)
    num += 1

# 문제 ) 숫자 2개를 입력받고 사이의 정수를 출력
num1 = int(input("숫자 1을 입력하세요 >>> "))
num2 = int(input("숫자 2를 입력하세요 >>> "))
count = 0

# 문제 ) 위의 리스트 양수 갯수 출력, 음수 갯수 출력, 짝수 갯수 출력
# 문제 ) 값을 입력받고 인덱스를 출력 ==> 예) 0 ==> 1, -6 ==> 4
# 문제 ) 위 리스트 안에서 가장 큰 값을 출력 ==> 예) 2005

