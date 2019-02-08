# 순차탐색
# 리스트에서 특정 숫자의 위치찾기
# 입력 : 리스트 a, 찾는값 x
# 출력 : 찾으면 그 값의 위치, 찾지 못하면 -1

def search_list(a, x):
    n = len(a)          # 길이재서
    for i in range(0, n):   #길이만큼 반복, 인덱스 0 ~
        if x== a[i]:
            return i    #위치 돌려줌
    return -1           #마지막 까지 비교해도 없으면 -1

lst = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(lst, 92))
print(search_list(lst, 33))  # 리스트에 두번나오지만 처음나온 위치만 출력.
print(search_list(lst, 100)) # -1 (리스트에 없음)