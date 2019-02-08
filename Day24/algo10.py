# 병합 정렬

#level.1
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def merge_sort(a):
    n = len(a)
    # 종료조건 : 정렬할 리스트의 자료 개수가 한개 이하이면 정렬할 필요 없음.
    if n<=1:
        return a

    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2                # 중간을 기준으로 두그룹으로 나눔
    g1 = merge_sort(a[:mid])    # 재귀 호출로 첫번째 그룹 정렬
    g2 = merge_sort(a[mid:])    # 재귀 호출로 두번째 그룹 정렬

    # 두 그룹을 하나로 병합
    result = []                 # 두 그룹을 합쳐 만들 최종 결과 리스트 준비
    while g1 and g2:            # 두 그룹 모두 자료가 남아있는 동안 반복
        if g1[0] < g2[0]:       # 두 그룹 맨 앞자료 값 비교
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    # 아직남아있는 자료들을 결과에 추가
    # g1과 g2중 이미 빈것은 while을 바로 지나감.
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

lst = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(lst))

#level.2
def merge_sort2(a):
    n = len(a)
    if n <= 1:
        return
    mid  = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g1[i2]
        i2 += 1
        ia += 1


lst = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort2(lst))




















