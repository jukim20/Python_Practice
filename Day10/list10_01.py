import random

# 리스트 함수

# 1. 추가 (append) ***
lst = [1, 2, 3]
lst.append(5)

print(lst)

lst = []
# 문제 1) 위 리스트 (빈 리스트) 에 랜덤 0~100 사이의 숫자 4개를 저장해보세요. (반복문 사용)
i = 0
while i < 4:
    num = random.randint(0, 100)
    lst.append(num)
    i += 1
print(lst)

# 2. 확장 (extend) 리스트 + 리스트
# append 와 다른 점: 리스트와 리스트를 append 할 시 리스트 속 리스트가 생기고, extend 할 시 1개의 리스트가 된다

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)

print(lst1)

# 3. 삽입 (위치, 값)
lst = [1, 2, 3]
lst.insert(0, 10)
print(lst)  # [10, 1, 2, 3]  # index 0의 위치에 10의 값을 삽입한다

# 4. 삭제 ***
# del(lst)  # 리스트 자체가 사라짐. 에러가 남.
# print(lst)  # NameError:  # lst 라는 variable 이 없어짐
print(lst)  # [10, 1, 2, 3]
del(lst[0])
print(lst)  # [1, 2, 3]
del(lst[0])
print(lst)  # [2, 3]

# 5. 값 삭제 (remove)
# 이미 값을 알고 있을 때 값만 없앰. 다만 처음 발견한 항목만 삭제 (중복 삭제 x)
lst = [10, 20, 40, 50, 60, 70, 20]
lst.remove(20)  # [10, 40, 50, 60, 70, 20]
print(lst)

# 6. 정렬 (sort)
lst = [20, 10, 4, -9]
lst.sort()
print(lst)  # [-9, 4, 10, 20]

# 7. 뒤집기 (reverse)
lst.reverse()
print(lst)  # [20, 10, 4, -9]

# 8. max, min
print(max(lst))  # 20
print(min(lst))  # -9

