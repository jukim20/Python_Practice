class Car:
    def init(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.dir = 0

    def speed_up(self):
        self.speed = int(input("속도를 입력하세요 >>> "))

    def go_forward(self):
        self.y += self.speed

    def turn_left(self):
        self.x -= self.speed

    def turn_right(self):
        self.x += self.speed

    def show_pos(self):
        print(self.x, ",", self.y)

    def controller(self):
        while True:
            print("*** 컨트롤러 ***")
            print("0. 속도조절")
            print("1. 전진")
            print("2. 좌회전")
            print("3. 우회전")
            print("4. 위치")
            print("5. 종료")

            sel = int(input("번호를 입력하세요 >>> "))
            if sel == 0:
                self.speed_up()
            elif sel == 1:
                self.go_forward()
            elif sel == 2:
                self.turn_left()
            elif sel == 3:
                self.turn_right()
            elif sel == 4:
                self.show_pos()
            elif sel == 5:
                print("종료됩니다.")
                break
            else:
                print("잘못 입력했습니다.")


c1 = Car()
c1.init()
c1.controller()
c1.show_pos()

c2 = Car()
c2.init()
c2.show_pos()