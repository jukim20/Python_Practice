# 선택정렬 
# 작은수 -> 큰수로 정렬

#level.1
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트
# 주어진 리스트에서 최소값의 위치를 돌려주는 함수

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []     # 새리스트를 만들어 정렬된 값을 저장
    while a:        # 주어진 리스트에 값이 남아있는 동안 계속
        min_idx = find_min_idx(a)       # 리스트에 남아 있는 값 중 최소값의 위치
        value = a.pop(min_idx)          # 찾은 최소값을 빼내어 value에 저장
        result.append(value)            # value를 결과 리스트 끝에 추가
    return  result

lst = [35,9,2,85,17]
print(sel_sort(lst))


#level.2
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬됨)

def sel_sort2(a):
    n = len(a)
    for i in range(0, n-1): # 0 ~ n-2까지 반복
        #i번 위치부터 끝까지 자료 값 중 최소값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
            #찾은 최소값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i]

lst1 = [2,4,5,1,3]
sel_sort2(lst1)
print(lst1)