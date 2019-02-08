
# 딕셔너리 (dictionary)
"""
1. 사전에서 "단어를 기준으로 해설" 을 찾듯이
    "키를 기준으로 값" 을 찾는 기능을 제공한다. ==> 키(인덱스)를 내가정한다.
2. 구조 { key1 : value1 , key2 : value2 , key3 : value3 ...}
3. key 는 변하지않는다.
4. 순서가 없다
"""
lst = [1, 2]  # 값만저장할수 있고 인덱스 는 자동으로 0~ 순차적으로 저장
print(lst[0])

dict1 = {0: 1, 1: 2, 2: 3, 3: 4}
print(dict1[0])

dict1 = {"0": 1, "1": 2, "철수": 3, 3: 4}
print(dict1["철수"])

dict1 = {"name": "김철수", "핸드폰": "010-222-333", "생일": "03/20"}
print(dict1["name"])  # 김철수
print(dict1["핸드폰"])  # 010-222-333
print(dict1["생일"])  # 3/20
dict1[1] = "하이"
print(dict1)  # {'name': '김철수', '핸드폰': '010-222-333', '생일': '03/20', 1: '하이'}
dict1["나이"] = 20
print(dict1)  # {'name': '김철수', '핸드폰': '010-222-333', '생일': '03/20', 1: '하이', '나이': 20}

del(dict1[1])

print(dict1)  # {'name': '김철수', '핸드폰': '010-222-333', '생일': '03/20', '나이': 20}

print(dict1.keys())  # dict_keys(['name', '핸드폰', '생일', '나이'])
print(dict1.values())  # dict_values(['김철수', '010-222-333', '03/20', 20])
print(dict1.items())  # dict_items([('name', '김철수'), ('핸드폰', '010-222-333'), ('생일', '03/20'), ('나이', 20)])

st_info = [
    {"이름": "kim", "나이": 21, "python": 10, "java": 70, "c": 100},
    {"이름": "park", "나이": 24, "python": 29, "java": 40, "c": 11},
    {"이름": "lee", "나이": 30, "python": 60, "java": 90, "c": 60},
    {"이름": "kang", "나이": 16, "python": 30, "java": 60, "c": 40}
]
total = 0
for i in st_info:
    total += i["c"]  # 211  c 만 다 더한 합
print(total)  # 211


# 전과목 총합 평균
total = 0

for i in st_info:
    total += i["python"] + i["java"] + i["c"]

avg = int(total / (len(st_info) - 1))
print(avg)

# 과목별 총합 평균

# 나이 평균
# 전과목합이 가장낮은 학생

# 제일 점수가 낮은 학생

# 나이 가 20세이 이하인 학생 정보 삭제

# 총점 항목을 추가 "총점": ???
for i in st_info:
    tot = 0
    tot += i["c"] + i["java"] + i["python"]
    i["total"] = tot

print(st_info)