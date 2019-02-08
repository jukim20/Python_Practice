# 리스트
# 이중반복문 문제
# 문제 1) 구구단 전체 출력
# 문제 2) 별찍기
"""
%%%%
%%%
%%
%
"""
for i in range(4):
    for j in range(4, i, -1):  # 시작 , 종료 , 간격
        print("&", end="")
    print()
APT = [[101, 102, 103, 104],
       [201, 202, 203, 204],
       [301, 302, 303, 304]]
PAY = [[1000, 2010, 3010, 2100],
       [7200, 4200, 2200, 5200],
       [5300, 3800, 11300, 3300]]
# 아파트 관리비 문제
for i in range(3):
    for j in range(4):
        print(PAY[i][j], end=" ")
    print()
# 0. 전체 관리비 합계
total = 0
for i in range(3):
    for j in range(4):
        total += PAY[i][j];
print("전체: ", total)
# 1. 각층별 관리비 합계
total = 0
for i in range(3):
    total = 0
    for j in range(4):
        total += PAY[i][j];
    print("각층별: ", total)
# 2. 우리집은 202호 우리집 관리비 출력
for i in range(3):
    for j in range(4):
        if APT[i][j] == 202:
            print(PAY[i][j])
# 3. 우리집관리비와 201호 관리비가 바꿔서 나왔다
#    교환후 출력
ii = 0
jj = 0
iii = 0
jjj = 0
for i in range(3):
    for j in range(4):
        if APT[i][j] == 201:
            ii = i
            jj = j
        if APT[i][j] == 202:
            iii = i
            jjj = j
temp = PAY[ii][jj]
PAY[ii][jj] = PAY[iii][jjj]
PAY[iii][jjj] = temp

for i in range(3):
    for j in range(4):
        print(PAY[i][j], end=" ")
    print()

# 4. 가장 관리비 많이 나온집 호수 출력
# 5. (심화) 가장 많이 나온집 순서대로 출력 ==> 1차원 리스트


