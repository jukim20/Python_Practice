"""
1. 입력 출력
2. 자료구조 ==> 1. 변수, 2. 리스트, (3. 클래스)
3. 알고리즘 ==> 1. 연산자, 2. if (조건문) 3. 반복문 (while), 4. 이중반복문 )\
"""
lst = []
for i in range(5):  # [0, 1, 2, 3, 4]
    pass
for i in lst:
    pass

# 문제) 랜덤으로 5명의 성적을 저장하고 성적이 60 이상인 번호, 점수 출력

num = 0
if num == 0:
    if num > 0:
        pass

for i in range(5):
    print("=================================")
    for n in range(5):  # i 1번째 n 5번, i 2번째 n 5번 .... 총 25번 반복 (i 는 가로, n은 세로)
        print(i, ",", n)

# 문제 1)
"""
$$$$$
$$$$$
$$$$$
"""

for i in range(3):
    for n in range(5):
        print("$", end="")
        if n % 5 == 4:
            print()

"""
#
##
###
####
"""

for i in range(2):
    for n in range(5):
        print("#", end="")
        count = 0
        if n == count:
            print()
        count += 1

"""
   &
  &&
 &&&
&&&&
"""