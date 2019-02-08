# 클래스 멤버함수 :
"""
    1. 정의하는법
        def + 이름 +(self) :
            self.변수명
    2. 사용하는법
        변수.함수이름()
"""
class Card:pass
class Person:
    card1 = Card()
    card2 = Card()
class Student:
    name = ""
    score = 0
    phone = ""
    def show_info(self):
        print(self.name)
        print(self.score)
        print(self.phone)
    def add_info(self):
        self.name = input("이름")
        self.score = int(input("점수"))
        self.phone = input("전화번호")
st_info = []
st_info_list = []
while True:
    print("** 학생 관리 프로그램 **")
    print("1. 등록")
    print("2. 삭제")
    print("3. 조회")
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        s1 = Student()
        s1.add_info()
        # s1.name = input("이름")
        # s1.score = int(input("점수"))
        # s1.phone = input("전화번호")
        st_info_list.append(s1)
        # st_info.append(input("이름"))
        # st_info.append(int(input("점수")))
        # st_info.append(input("전화번호"))
        # st_info_list.append(st_info)
    if sel == 2: pass
    if sel == 3:
        for i in range(len(st_info_list)):
            st_info_list[i].show_info()
            # print(st_info_list[i].name)
            # print(st_info_list[i].score)
            # print(st_info_list[i].phone)

