lst = [10, 20, 30, 40, 50]

# 문제 1) 인덱스를 입력받고 해당 값을 출력

index = int(input("인덱스를 입력하세요 >>> "))
print(lst[index])

print("=============================================")

# 문제 2) 인덱스를 2개 입력받고 해당 값의 합을 출력
index1 = int(input("인덱스 1을 입력하세요 >>> "))
index2 = int(input("인덱스 2를 입력하세요 >>> "))

if 0 <= index1 <= 4 and 0 <= index2 <= 4:
    print(lst[index1] + lst[index2])
else:
    print("잘못 입력했습니다")

print("=============================================")

# 문제 3) 인덱스를 2개 입력받고 해당 값을 교환 후 전체 출력
index1 = int(input("인덱스 1을 입력하세요 >>> "))
index2 = int(input("인덱스 2를 입력하세요 >>> "))

if 0 <= index1 <= 4 and 0 <= index2 <= 4:
    orig_index1 = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = orig_index1
    print(lst)
else:
    print("잘못 입력했습니다.")

print("=============================================")

# 문제 4) 값을 입력받고 인덱스를 출력
lst = [10, 20, 30, 40, 50]
i = 0

val = int(input("값을 입력하세요 >>> "))

if val not in lst:
    print("해당 값을 가진 인덱스가 없습니다.")
else:
    while i < 5:
        if val == lst[i]:
            print("인덱스 : ", i)
            break   # 보조제어문 ==> 반복문을 즉시 종료시킨다.
        i += 1
