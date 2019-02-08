# 리스트의 슬라이싱 및 인덱싱

lst = [1, 2, 3, [4, 5, 6]]
print(lst)  # [1, 2, 3, [4, 5, 6]]

print(lst[0])  # 1
print(lst[2])  # 3
print(lst[3])  # [4, 5, 6]
print(lst[3][0])  # 4

# 슬라이싱
lst = [1, 2, 3, 4, 5, 6]
print(lst[0:3])  # [1, 2, 3] : 0 <= ?? <3

lst = [1, 2, 3, ["a", "b", "c"], 4, 5]
print(lst[2:4])  # [3, ['a', 'b', 'c']]

# 문제 1) [b, c]
print(lst[3][1:3])

print("============================================================")

lst = [-9, 0, 10, 5, -6, 1, 100]
# 문제 1) 위의 리스트 전체 양수 갯수 출력, 음수 갯수 출력, 짝수 갯수 출력
i = 0
pos_count = 0
neg_count = 0
even_count = 0

while i < 7:
    if lst[i] > 0:
        pos_count += 1
    if lst[i] < 0:
        neg_count += 1
    if lst[i] % 2 == 0:
        even_count += 1
    i += 1
print("양수의 갯수 : ", pos_count, "음수의 갯수 : ", neg_count, ", 짝수의 갯수 : ", even_count)

print("============================================================")

names = ["박병욱", "김철수", "김민수", "박영희", "박민수"]
scores = [20, 100, 60, 23, 90]
# 문제 2) 이름을 입력하면 해당 점수가 출력
end = False
i = 0

while not end:
    val = input("이름을 입력하세요 >>> ")
    if val == "quit":
        print("종료 되었습니다.")
        end = True
    elif val not in names:
        print("잘못 입력했습니다.")
    else:
        while i < 5:
            if val == names[i]:
                print("점수 : ", scores[i])
                break
            i += 1
