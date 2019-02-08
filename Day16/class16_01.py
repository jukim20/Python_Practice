class Card:
    def init(self):
        self.card_shape = ["◆", "♠", "♥", "♣"]
        self.card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.shape = ""
        self.num = 0

class Deck:
    def init(self):  # 초기화 , 시작
        self.c1 = Card()
        self.c1.init()
        self.deck = []
        for i in range(40):
            self.temp = []  # 초기화 해주어야하기 때문에 for 문 안에 들어와있어야함
            self.temp.append(self.c1.card_shape[i % 4])
            self.temp.append(self.c1.card_num[i // 4])
            self.c1.shape = self.temp[0]
            self.c1.num = self.temp[1]
            self.deck.append(self.c1)

    def show_info(self):
        for i in range(40):
            print(self.deck[i], end=" ")
            if i % 4 == 3:
                print()

    def shuffle(self):
        import random
        for i in range(100):  # 100번섞기
            self.rand = random.randint(0, 39)
            self.temp = self.deck[self.rand]
            self.deck[self.rand] = self.deck[0]
            self.deck[0] = self.temp

# deck1 = Deck()
# deck1.init()
# deck1.show_info()

# c1 = Card()
# deck = []
# for i in range(40):
#     temp = []  # 임시로 한장씩 만든다음 deck 에 추가
#     temp.append(c1.card_shape[i % 4])
#     temp.append(c1.card_num[i // 4])
#     deck.append(temp)
# for i in range(40):
#     print(deck[i], end=" ")
#     if i % 4 == 3:
#         print()
