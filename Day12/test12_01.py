# 예) lst1 =[1,2,3] lst2 = [4,5,6] lst_result = [5,7,9]
# 응용문제 5) 리스트 2개를 인자로 사용하되 다른길이의 리스트 를 사용해서 + 출력
# 만약에 같은 자리의 값이 없으면 그냥 출력
# 예) lst1 = [1,2,3,4]  lst2 = [5,6] lst_result = [6,8,3,4]
def add_list(lst1, lst2):
    lst3 = []
    for i in range(len(lst1)):  # 길이를 재서 같은인덱스의 값끼리 더한다.
        lst3.append(lst1[i] + lst2[i])
    print(lst3)
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
add_list(lst1, lst2)
# =================================================
def lst_add2(lst1, lst2):
    if len(lst1) < len(lst2):  # 길이가 짧은걸찾는다.
        temp = lst1
        lst1 = lst2
        lst2 = temp
    a = len(lst1)
    b = len(lst2)
    lst3 = []
    for i in range(b):  # 짧은길이만큼 먼저 더해준다
        lst3.append(lst1[i] + lst2[i])
    while b < a:  # 나머지는 그냥 추가
        lst3.append(lst1[b])
        b += 1
    print(lst3)
lst1 = [1, 2, 3]
lst2 = [4, 5, 8, 7, 4]
lst_add2(lst1, lst2)