import random

# for 문
# 반복문 while 보다 조금 더 간단하게 사용 가능하다
#   1. for ==> 키워드
#   2. 변수 in 리스트 ==> 리스트의 내용을 하나씩 임시로 저장 (리스트 갯수만큼)
#   3.
num = 0
while num < 3:
    print(num)
    num += 1

for i in range(3):  # i 의 초기값과 증가문 필요 x  # 0 부터 3 까지 i 에 한번씩 저장 [0, 1, 2]
    print(i)

for i in [0, 1, 2]:  # 0 부터 3 까지 i 에 한번씩 저장 [0, 1, 2]
    print(i)

for i in [10, 20, 30, 40, 50]:
    print(i)
print("===========================================")

# 0~10 사이에서 짝수만 출력
for i in range(11):
    if i % 2 == 0:
        print(i)
print("===========================================")

# 0~10 사이에서 홀수만 다 더한값 출력
sum = 0
for i in range(11):
    if i % 2 == 1:
        sum += i
print(sum)
print("===========================================")

# 리스트에 0~100까지 랜덤으로 5명 저장 (for 사용)
# 조건) 성적이 60 이상인 번호, 점수 출력
lst = []
for i in range(6):
    rand = random.randint(0, 100)
    lst.append(rand)

print(lst)
print("===========================================")

print("성적이 60 이상인 사람 >>> ")
for i in range(6):
    if lst[i] >= 60:
        print("번호 : ", i, ", 점수 : ", lst[i])