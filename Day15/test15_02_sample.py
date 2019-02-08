# 정렬
lst = [1, 3, 54, 23, 5, 67, 7, 3, 4]
# lst = [67, 3, 54, 23, 5, 1, 7, 3, 4]
# lst = [67, 54, 3, 23, 5, 1, 7, 3, 4]
# lst = [67, 54, 23, 3, 5, 1, 7, 3, 4]
# lst = [67, 54, 23, 7, 5, 1, 3, 3, 4]
# lst = [67, 54, 23, 7, 5, 4, 3, 3, 1]
APT = [[101, 102, 103, 104],
       [201, 202, 203, 204],
       [301, 302, 303, 304]]
PAY = [[1000, 2010, 3010, 2100],
       [7200, 4200, 22200, 5200],
       [5300, 3800, 11300, 3300]]
# 4. 가장 관리비 많이 나온집 호수 출력
# 5. (심화) 가장 많이 나온집 순서대로 출력 ==> 1차원 리스트
max1 = PAY[0][0]
x = 0
y = 0
for i in range(3):
    for j in range(4):
        if max1 < PAY[i][j]:
            max1 = PAY[i][j]
            x = i
            y = j
print(APT[x][y])
APT_sort = []
PAY_sort = []
for i in range(3):
    for j in range(4):
        APT_sort.append(APT[i][j])
        PAY_sort.append(PAY[i][j])
print(APT_sort)
print(PAY_sort)









