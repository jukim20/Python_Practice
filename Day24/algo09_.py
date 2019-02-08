# 삽입정렬
# level.1
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r,v):
    # 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인
    for i in range(0, len(r)):
        # v값보다 i번 위치에 있는 자료 값이 크면
        # v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨.
        if v < r[i]:
            return i
    # 적절한 위치를 못 찾았을 때는
    # v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입.
    return len(r)

def ins_sort(a):
    result = []     # 새리스트 만들어 정렬된 값을 저장
    while a:        # 기존 리스트에 값이 남아있는 동안 반복
        value = a.pop(0)    # 기존 리스트에서 한개를 꺼냄
        ins_idx = find_ins_idx(result, value)   # 꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx, value)           # 찾은 위치에 값 삽입(이후 값은 한 칸씩 밀려남)
    return result

# level.2 : 일반적인 형태
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def ins_sort(a):
    n = len(a)
    for i in range(1, n):   # 1부터 n-1까지
        key = a[i]          # i번 위치에 있는 값을 key에 저장
        # j를 i 바로 왼쪽 위치로 저장
        j = i-1
        # 리스트의 j번 위치에 있는 값과 key를 비교해서 key가 삽입될 적절한 위치를 찾음.
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]     # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1

        a[j+1] = key            # 찾은 삽입 위치에 key를 저장

d = [2,4,5,1,3]
ins_sort(d)
print(d)