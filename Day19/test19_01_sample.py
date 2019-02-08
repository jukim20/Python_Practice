#  변수 리스트
#  연산자 조건문 반복문 2중반복문
# 함수 연습
def show_line():
    print("=============================================")
show_line()
def show_num(num):
    print(num)
show_num(10)
# 문제1 ) 인자로 정수 1개를 사용해서 정수만큼 그려주는 함수를 만들자.
# 문제2 ) 인자로 정수 1개를 사용해서 0~ 정수만큼 다더해주는 함수를 만들자.
# 문제3 ) 인자 2개를 사용해서 사칙연산 출력
# 문제4 ) 인자 2개를 사용해서 2정수 사이의 합출력 예) 1,  6 ==> 1+2+3+4+5+6
#  클래스
class Clothes:
    def set_info(self, k, p):  # T , C , P , S
        self.kind = k
        self.price = p
        self.count = 0
class Shop:
    t_list = []
    c_list = []
    p_list = []
    s_list = []
    def set_items(self):
        self.item = Clothes()
        self.item.set_info("반팔 t", 100)
        self.t_list.append(self.item)
        self.item = Clothes()
        self.item.set_info("긴팔 t", 1000)
        self.t_list.append(self.item)
        self.item = Clothes()
        self.item.set_info("롱코트 ", 1000)
        self.c_list.append(self.item)
        self.item = Clothes()
        self.item.set_info("롱코트 ", 1000)
        self.c_list.append(self.item)
    def show_items(self , num):
        if num == 1:
            number = 0
            for i in self.t_list:
                number += 1
                print(number, "번", i.kind, i.price)
            sel = int(input("번호를 입력하세요 "))
            del(self.t_list[number])
        if num == 2:
            for i in self.c_list:
                print(i.kind, i.price)
        # 1. 티셔츠 2. 코트 3. 바지 4. 치마
    def show_menu(self):
        while True:
            print("코리아 상점")
            print("1.티셔츠")
            print("2.코트")
            sel = int(input("번호를 입력하세요"))
            if sel == 0: break
            self.show_items(sel)
class MyInven:pass
# shop  옷 ==> 티셔츠 코트 바지 치마 등등 ==> 가격 개수
# 1.구입 ==> 내 인벤에 저장 되게 만들어보자
s1 = Shop()
s1.set_items()
s1.show_menu()
