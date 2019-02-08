#  문제는 각자 레벨에 맞춰서 골라서 푸세요~

#  if 문제 ) 숫자 하나를 입력받고 "짝수" , "홀수" 출력

#  반복문 문제 ) 0~10 중에서 홀수 만 출력

#  문제 ) 0~10중에서 전부 더한값 출력
lst = [-9, 0, 10, 2005, -6, 21, 100]
# 리스트 문제 ) 위의 리스트 안의 각요소의 총합을 출력
total = 0
num = 0
while num < len(lst):
    total = total + lst[num]
    num += 1
print("총합 : ", total)
print("==========================================")

# 문제 ) 위의 리스트 에서 음수의 갯수를 출력
num = 0
neg_count = 0
while num < len(lst):
    if 0 > lst[num]:
        neg_count += 1
    num += 1
print("음수의 갯수 : ", neg_count)
print("==========================================")

# 문제 ) 위의 리스트 에서 인덱스 두개를 입력받고 서로 교환
print(lst)
i1 = int(input("인덱스 1을 입력하세요 >>> "))
i2 = int(input("인덱스 2를 입력하세요 >>> "))

temp = lst[i1]
lst[i1] = lst[i2]
lst[i2] = temp
print(lst)
print("==========================================")

bingo = [0, 0, 0, 0, 0, 0, 0]
# 문제 1) 인덱스를 입력받으면 해당 요소의 값을 3으로 변경
end = False
while not end:
    i = int(input("인덱스 (0~6)를 입력하세요 (종료: 7) >>> "))
    if i < len(bingo):
        bingo[i] = 3
        print(bingo)
    elif i == 7:
        end = True
    else:
        print("잘못 입력했습니다.")


# 문제 2) 3이 연속으로 3줄이상이면 "빙고" 출력

