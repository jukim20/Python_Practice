import pygame
class MyRect:
    def set_info(self, color, pos, size):
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.speed = 3
        self.isUp = False
        self.isDown = False
        self.bulletList = []
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed
    def update(self):
        if self.isUp:
            self.move_up()
        if self.isDown:
            self.move_down()
        if self.y > 400:
            self.isDown = False
    def keyManager(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.isUp = True
            if event.key == pygame.K_DOWN:
                self.isDown = True
            if event.key == pygame.K_SPACE:
                self.bullet = MyRect()
                self.bullet.set_info((0, 0, 255), (self.x, self.y), (20, 20))
                self.bullet.isDown = True
                self.bulletList.append(self.bullet)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.isUp = False
            if event.key == pygame.K_DOWN:
                self.isDown = False
