import random


class Enemy(ImgBase):
    def __init__(self, x, y, w, h, speed):
        super().__init__("bat.png", x, y, w, h, speed)

    def move(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = 900
            self.y = (random.randint(0, 300))
    def render(self, gamepad):
        gamepad.blit(self.img, (self.x , self.y))