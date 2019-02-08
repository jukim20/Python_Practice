class Bullet(ImgBase):
    def __init__(self, x, y, w, h, speed):
        super().__init__("imgbtn_blue_normal.png", x, y, w, h, speed)
    def move(self):
        self.x += self.speed
    def render(self, gamepad):
        gamepad.blit(self.img, (self.x , self.y))
    def collision(self, enemy):

        self.enemyleft = enemy.x
        self.enemyright = enemy.x + enemy.w
        self.enemytop = enemy.y
        self.enemybottom = enemy.y + enemy .h

        print(self.enemyleft , " ," , self.enemyright , "," , self.enemytop, " ,", self.enemybottom)
        print(self.x ,",", self.y)
        # 충돌조건
        if self .x >= self.enemyleft and self.x <= self.enemyright and \
                        self.y >= self.enemytop and self.y <= self.enemybottom:
            return True
        return False