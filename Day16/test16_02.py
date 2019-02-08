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

    def show_channel(self):
        print(self.channel)
        if self.channel == 1:
            print("드라마")
        elif self.channel == 2:
            print("스포츠")
        elif self.channel == 3:
            print("애니메이션")
        else:
            print("치지직")

    def channel_up(self):
        self.channel += 1
        self.show_channel()

    def channel_down(self):
        self.channel -= 1
        self.show_channel()


t2 = Tv2()
t2.init("삼성", 40, 500000)
t2.show_info()
t2.channel_up()

t3 = Tv2()
t3.init("엘지", 60, 2000000)
t3.show_channel()  # 기본이 0 번이고 채널을 바꾸지 않았으니 치지직

himart = []
himart.append(t2)
himart.append(t3)


class Car:  # 전진 , 좌회전 , 우회전 , 위치
    x = 0
    y = 0

    def show_location(self):
        self.location = (self.x, self.y)
        print(self.location)

    def move(self):
        sel = (input("동작을 입력하세요 \n"
                     "전진 : f , 후진 : b , 좌회전 : l , 우회전 : r \n"
                     ">>> "))
        if sel == "f":
            self.y += 1
        elif sel == "b":
            self.y -= 1
        elif sel == "l":
            self.x -= 1
        elif sel == "r":
            self.x += 1
        else:
            print("잘못 입력했습니다.")
        self.show_location()


c1 = Car()
c1.show_location()
c1.move()
c1.move()
c1.move()

himart.append(c1)

