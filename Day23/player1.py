import pygame


class Player(ImgBase):
    def __init__(self, x, y, w, h, speed):
        super().__init__("plane.png", x, y, w, h, speed)
        self.isLeft = False
        self.isRight = False
        self.bullets = []
    def keyDown(self, key):
        self.key = key
        if self.key == pygame.K_d:
            self.isRight = True
        if self.key == pygame.K_a:
            self.isLeft = True
        if self.key == pygame.K_SPACE:
            self.bullets.append(Bullet(self.x, self.y, 10, 5, 10))
    def keyUp(self, key):
        self.key = key
        if self.key == pygame.K_d:
            self.isRight = False
        if self.key == pygame.K_a:
            self.isLeft = False
    def move(self):
        if self.isRight == True:
           self.x += self.speed
        if self.isLeft == True:
           self.x -= self.speed
    def render(self, gamepad):
        gamepad.blit(self.img , (self.x , self.y))
