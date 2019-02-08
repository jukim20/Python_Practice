lst = [-9, 0, 10, 2005, -6, 21, 100]

# 문제 1) 인덱스를 입력받고 값 출력
i = int(input("인덱스 (0~6) 를 입력하세요 >>> "))
if i < len(lst):
    print("값 : ", lst[i])
else:
    print("잘못 입력했습니다.")

print("==========================================")

# 문제 2) 값을 입력받고 인덱스 출력
val = int(input("값을 입력하세요 >>> "))
if val not in lst:
    print("해당 값을 가진 인덱스가 없습니다.")
else:
    i = 0
    for i in range(len(lst)):
        if val == lst[i]:
            print("인덱스 : ", i)

print("==========================================")

# 문제 3) 음수의 갯수, 짝수의 갯수
neg_count = 0
pos_count = 0

for i in range(len(lst)):
    if lst[i] < 0:
        neg_count += 1
    elif lst[i] > 0:
        pos_count += 1
print("음수의 갯수 : ", neg_count, ", 짝수의 갯수 : ", pos_count)

print("==========================================")

# 문제 4) 가장 큰 값 찾기

max = lst[0]
for i in range(len(lst)):
    if max > lst[i]:
        pass
    else:
        max = lst[i]
print("가장 큰 값 : ", max)

print("==========================================")

# 심화문제 5) 인덱스 2개를 입력받고 서로 교환
print(lst)
i1 = int(input("인덱스 1 (0~6)을 입력하세요 >>> "))
i2 = int(input("인덱스 2 (0~6)를 입력하세요 >>> "))

if 0 <= i1 < len(lst) and 0 <= i2 < len(lst):
    temp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = temp
else:
    print("잘못 입력했습니다.")
print(lst)

print("==========================================")

lst = ["읏", 0, 0, 0, 0, 0]
print(lst)
#  a, d 를 입력하면 "읏" 이 오른쪽 왼쪽 이동
end = False

while not end:
    sel = input("방향을 입력하세요 (a 왼쪽, d 오른쪽 >>> ")
    if sel == "a":
        for i in range(len(lst)):
            if lst[i] == "읏":
                temp = lst[i]
                lst[i] = lst[i-1]
                lst[i-1] = temp
    elif sel == "d":
        for i in range(len(lst)):
            if lst[i] == "읏":
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp


lst = [10, 11, 12, 13, 14, 15, 16, 17, 18]
