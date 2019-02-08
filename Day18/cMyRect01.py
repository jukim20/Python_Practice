import pygame  # 60 프레임 , x y , 이벤트 처리
import random


class MyRect:
    def set_info(self, color, pos, size):
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.speed = 3
        self.isUp = False
        self.isDown = False
        self.isRight = False
        self.isLeft = False
        self.bulletList = []

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def move_right(self):
        self.x += self.speed

    def move_left(self):
        self.x -= self.speed

    def update(self):
        if self.isUp:
            self.move_up()
        if self.isDown:
            self.move_down()
        if self.isLeft:
            self.move_left()
        if self.isRight:
            self.move_right()

    def keyManager(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bullet = MyRect()
                self.bullet.set_info((0, 255, 255), (self.x, self.y), (20, 20))
                self.bullet.isRight = True
                self.bulletList.append(self.bullet)

