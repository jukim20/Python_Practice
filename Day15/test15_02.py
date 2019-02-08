# 정렬
import random

"""
lst = [1, 3, 54, 23, 5, 67, 7, 3, 4]
lst = [67, 3, 54, 23, 5, 1, 7, 3, 4]
lst = [67, 54, 3, 23, 5, 1, 7, 3, 4]
lst = [67, 54, 23, 3, 5, 1, 7, 3, 4]
lst = [67, 54, 23, 7, 5, 1, 3, 3, 4]
lst = [67, 54, 23, 7, 5, 4, 3, 3, 1]
"""


def create_lst():
    lst = []
    for i in range(9):
        rand = random.randint(1, 100)
        lst.append(rand)
    print(lst)
    return lst


rand_lst = create_lst()


def find_max(lst):
    max = lst[0]
    for i in range(len(lst)):
        if max > lst[i]:
            pass
        else:
            max = lst[i]
    return max


APT = [[101, 102, 103, 104],
       [201, 202, 203, 204],
       [301, 302, 303, 304]]
PAY = [[1000, 2010, 3010, 2100],
       [7200, 4200, 2200, 5200],
       [5300, 3800, 11300, 3300]]
# 아파트 관리비 문제
# 가장 관리비 많이 나온 집 호수 출력
# 가장 많이 나온집 순서대로 출력  ==> 1차원 리스트

max = PAY[0][0]
x = 0
y = 0

for i in range(3):
    for j in range(4):
        if max < PAY[i][j]:
            max = PAY[i][j]
            x = i
            y = j
print(APT[x][y])

"""
  *
 **
***
***
 **
  *
"""
