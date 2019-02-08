# 상속

"""
객체 지향의 가장 큰 장점은 코드의 재활용이다.
    1) 함수
    2) 클래스
1. 클래스를 여러개 사용하는 경우 :
    겹치는 멤버들 모두 똑같이 사용하는 경우 상속을 통해서 간결하게 만들 수 있다.

2. 상속해주는 클래스 : 부모 클래스
3. 상속받는 클래스 : 자식 클래스
4. 상속받는 방법 :
    class  자식클래스(부모클래스)


"""

class Player:
    def set_info(self):
        self.hp = 10
        self.att = 20
        self.deff = 30
        self.armor = 40
        self.weapon = 60
        self.magic = 70

    def show_info(self):
        print(self.hp)
        print(self.att)
        print(self.deff)
        print(self.armor)
        print(self.weapon)
        print(self.magic)


class Monster:  # 몬스터 200 종류; 일일이 다 적을 필요가 있는가? ==> 겹치는 건 빼자
    def set_info(self):
        self.hp = 20
        self.att = 30
        self.deff = 70
        self.weapon = 60

    def show_info(self):
        print(self.hp)
        print(self.att)
        print(self.deff)
        print(self.weapon)

