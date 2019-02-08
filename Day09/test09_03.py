import random

lst = [1, 2, 3, 4, 5, 6]

# 심화 ) 리스트의 요소들을 섞어보세요 ==> 예) 6, 5, 2, 1, 4, 3
count = 0
while count <= 100:
    i = random.randint(0, 5)
    real_1 = lst[1]
    lst[1] = lst[i]
    lst[i] = real_1
    count += 1
print(lst)

print("=========================================================")

# 기본문제 ) 위의 요소들의 합
sum = 0
i = 0
while i < 6:
    sum += i
    i += 1
print("합 : ", sum)

print("=========================================================")

# 인덱스를 입력하면 값 출력
i = int(input("인덱스 (0~5) 를 입력하세요 >>> "))

if i < 0 or i > 5:
    print("잘못 입력했습니다.")
else:
    print("해당 인덱스의 값 : ", lst[i])

print("=========================================================")

# 값을 입력하면 인덱스 출력
i = 0
val = int(input("값을 입력하세요 >>> "))
if val not in lst:
    print("해당 값을 가진 인덱스가 없습니다.")
else:
    while i < 6:
        if val == lst[i]:
            print("인덱스 : ", i)
        i += 1

print("=========================================================")

# 인덱스 2개를 입력하면 서로교환
i1 = int(input("인덱스 1을 입력하세요 >>> "))
i2 = int(input("인덱스 2를 입력하세요 >>> "))

if 0 <= i1 <= 5 and 0 <= i2 <= 5:
    real_i1 = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = real_i1
    print(lst)
else:
    print("잘못 입력했습니다.")

print("=========================================================")

# 가장 큰 수 찾기
i = 0
while i < 5:
    if lst[i] > lst[i+1]:
        win = lst[i]
    else:
        win = lst[i+1]
    i += 1
print("가장 큰 수 : ", win)

print("=========================================================")

# 응용문제 ) r을 입력받으면 10이 오른쪽으로 이동 ==>
# 예 ) l, r 을 입력하세요 ==> r ==> [20, 10, 30, 40, 50, 60]
# 예 ) l, r 을 입력하세요 ==> r ==> [20, 30, 10, 40, 50, 60]
# 예 ) l, r 을 입력하세요 ==> l ==> [20, 10, 30, 40, 50, 60]

lst = [10, 20, 30, 40, 50, 60]
print(lst)

end = False
while not end:
    dir = input("l (좌), r (우) 을 입력하세요. (종료 : q) >>> ")
    if dir == "l":
        i = 0
        val = 10
        while i < 6:
                if val == lst[i]:
                    i_10 = i
                i += 1
        temp = lst[i_10]
        lst[i_10] = lst[i_10-1]
        lst[i_10-1] = temp
        print(lst)
    elif dir == "r":
        i = 0
        val = 10
        while i < 6:
            if val == lst[i]:
                i_10 = i
            i += 1

        if i_10 < 5:
            temp = lst[i_10]
            lst[i_10] = lst[i_10+1]
            lst[i_10+1] = temp
        else:
            index = 5
            while index >= 0:
                lst[index] = lst[index-1]
                index -= 1
            lst[0] = val
        print(lst)
    elif dir == "q":
        end = True
        print("종료됩니다.")
    else:
        print("잘못 입력했습니다.")