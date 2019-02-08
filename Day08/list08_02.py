scores = [80, 39, 53, 21, 45, 64]

# 성적 검색 프로그램
# 인덱스를 입력받으면 해당 점수를 출력하게 만들어보세요 (반복문 사용)

end = False

while not end:
    index = int(input("인덱스 (0~5) 를 입력하세요 (종료 -1) >>> "))
    if 0 <= index <= 5:
        print("성적 : ", scores[index])
    elif index == -1:
        print("프로그램이 종료 되었습니다.")
        end = True
    else:
        print("잘못 입력했습니다.")

# 반복문을 사용하고 전체 합계와 평균 출력
print("========================================================")

index = 0
sum = 0

while index <= 5:  # 인덱스 범위 초과 예외처리
    sum += scores[index]
    index += 1

avg = sum / index
print("합계 : ", sum, "점, 평균 : ", avg, "점")