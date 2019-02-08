# 클래스
"""
정의 방법 : (설계도)
    class + 이름 :
        (멤버 변수)
        (멤버 함수)
선언 방법 :
    변수 + 클래스명 + ()
    예 ) p1 = Person()
사용 방법 :
    변수 + (.)dot + 내부변수
    예 ) p1.name = "김철수"

"""

class Person:
    name = ""
    age = 0


p1 = Person()
p1.name = "김철수"
p1.age = 20
p1.score = 70
print(p1.name, ",", p1.age)  # 김철수, 20

# 3번째
st_list = []
st_list.append(p1)
print(st_list[0].name)  # 0 번 학생의 이름

# 데이터를 하나로 묶는 것일뿐

# 1번째
name = ["김철수", "박만수"]
age = [20, 30]
score = [100, 90, 20]

print("이름 : ", name[0], ", 나이 : ", age[0], ", 성적 : ", score[0])

# 2번째
st_info = ["김철수", 20, 100]
st_info_list = []
st_info_list.append(st_info)
print(st_info_list[0][0])
# 총 리스트의 0 번 리스트는 0 번 학생. (st_info_list[0])
# 0번 학생의 이름은 0 인덱스 (st_info_list[0][0])
