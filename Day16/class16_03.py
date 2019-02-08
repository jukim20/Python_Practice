from Day16.class16_01 import Deck
from Day16.class16_02 import Person

p1 = Person()
p1.init()  # 초기화
p2 = Person()
p2.init()
d1 = Deck()
d1.init()
d1.shuffle()
# d1.show_info()
card_index = 0


def init():  # 전역변수를 사용할 수 없다 ==> 글로벌
    global card_index
    p1.card1 = d1.deck[card_index]
    p1.card2 = d1.deck[card_index + 1]
    p2.card1 = d1.deck[card_index + 2]
    p2.card2 = d1.deck[card_index + 3]
    card_index += 4;


def game():
    money = int(input("베팅 금액을 입력하세요 >>> "))
    print(p1.card1.num, ",", p1.card2.num)
    p1_num = p1.card1.num + p1.card2.num
    p2_num = p2.card1.num + p2.card2.num

    if p1_num > p2_num:
        print("이겼습니다!")
        p1.money += money
        p2.money -= money
        print(money)
    elif p1_num < p2_num:
        print("졌습니다.")
        p1.money -= money
        p2.money += money
        print(money)
    else:
        print("비겼습니다.")
        print(money)


print("*** 카드게임 ***")
init()
while True:
    game()
