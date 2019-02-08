# 저장 + 수정 ==> 클래스
# 저장 : 변수 , 리스트
# 수정 : 연산자 , 조건문 , 반복문 , 이중반복문
# 리스트.append(클래스)


class Tv:
    channel = 0
    size = 0
    brand = ""
    price = 0

    def show_info(self):
        print(self.brand)
        print(self.size)
        print(self.price)
        print(self.channel)


class Tv2:  # 특징 : 함수를 사용할 때는 self 를 꼭 사용해야한다.

    def init(self, b, s, p):
        self.brand = b
        self.size = s
        self.price = p
        self.channel = 0

    def show_info(self):
        print(self.brand)
        print(self.size)
        print(self.price)
        print(self.channel)

t1 = Tv()
t1.price = 500000
t1.size = 40
t1.brand = "삼성"  # 이렇게 할 수 있으나 덜 깔끔함
t1.show_info()

t2 = Tv2()
t2.init("엘지", 60, 1500000)
t2.show_info()

himart = []
himart.append(t1)
himart.append(t2)

