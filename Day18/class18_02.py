class Unit:  # 부모 (상위) 클래스
    def set_info(self):
        self.hp = 20
        self.att = 30
        self.deff = 70
        self.weapon = 60


class Player(Unit):
    def set_info(self):
        super().set_info()  # 부모 함수 호출  super() ==> 부모
        self.armor = 40
        self.magic = 70

    def show_info(self):
        print(self.hp)
        print(self.att)
        print(self.deff)
        print(self.armor)
        print(self.weapon)
        print(self.magic)


class Monster(Unit):
    def show_info(self):
        print(self.hp)
        print(self.att)
        print(self.deff)
        print(self.weapon)

m1 = Monster()
m1.set_info()
m1.show_info()

