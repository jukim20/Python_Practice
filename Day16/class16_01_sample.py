class Card:
    def init(self):
        self.card_shape = ["◆", "♠", "♥", "♣"]
        self.card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.shape = ""
        self.num = 0
class Deck:
    def init(self):
        self.c1 = Card()
        self.c1.init()
        self.deck = []
        for i in range(40):
            self.temp = []
            self.temp.append(self.c1.card_shape[i % 4])
            self.temp.append(self.c1.card_num[i // 4])
            self.c1.shape = self.temp[0]
            self.c1.num = self.temp[1]
            self.deck.append(self.c1)
            # print(self.temp)
    def shuffle(self):
        import random
        for i in range(100):  # 100번섞기
            self.rand = random.randint(0, 39)
            self.temp = self.deck[self.rand]
            self.deck[self.rand] = self.deck[0]
            self.deck[0] = self.temp
    def show_info(self):
        for i in range(40):
            print(self.deck[i], end=" ")
            if i % 4 == 3:
                print()
# deck1 = Deck()
# deck1.init()
# deck1.show_info()
# deck1.shuffle()
# deck1.show_info()