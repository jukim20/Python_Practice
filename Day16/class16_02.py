from Day16.class16_01 import Card
# from 폴더명.파일명 import * (전부 가져올때) 혹은 클래스명
# 예 ) from Day16.class16_01 import *


class Person:
    def init(self):
        self.card1 = Card()
        self.card1.init()
        self.card2 = Card()
        self.card2.init()
        self.money = 10000

    def show_info(self):
        print(self.card1)
        print(self.card2)
        print(self.money)


p1 = Person()
p1.init()
print(p1.card1.num)

