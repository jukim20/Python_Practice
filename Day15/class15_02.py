# 클래스 멤버 함수 :
"""
    1. 정의하는 법:
        def + 이름 + (self):
           self.변수명

    2. 사용하는 법
        변수.함수이름()
"""
class Card:pass

class Person:
    card1 = Card()
    card2 = Card()
    card3 = Card()



class Student:
    name = ""
    score = 0
    phone = ""

    def show_info(self):
        print("이름 : ", self.name, end=",  ")
        print("성적 : ", self.score, end=",  ")
        print("전화번호 : ", self.phone)

    def add_info(self):
        self.name = input("이름 >>> ")
        self.score = int(input("성적 >>> "))
        self.phone = input("전화번호 >>> ")


st_info_list = []

while True:
    print("** 학생 관리 프로그램 **")
    print("1. 등록")
    print("2. 삭제")
    print("3. 조회")
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        s1 = Student()  # 밖에다 만들면 안되고 매번 생성해줘야함
        s1.add_info()

        # s1.name = input("이름 >>> ")
        # s1.score = int(input("성적 >>> "))
        # s1.phone = input("전화번호 >>> ")
        st_info_list.append(s1)

    elif sel == 2:
        pass

    elif sel == 3:
        for i in range(len(st_info_list)):
            st_info_list[i].show_info()

        # for i in range(len(st_info_list)):
        # print("이름 : ", st_info_list[i].name, end=",  ")
        # print("성적 : ", st_info_list[i].score, end=",  ")
        # print("전화번호 : ", st_info_list[i].phone)

    elif sel == 4:
        print("시스템이 종료됩니다.")
        break
    else:
        print("잘못 입력했습니다.")




