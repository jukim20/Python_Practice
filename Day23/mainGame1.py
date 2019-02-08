import pygame
import random
class ImgBase:
    def __init__(self,filename, x, y, w, h, speed):
        self.img = pygame.image.load(filename)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

class Bullet(ImgBase):
    def __init__(self, x, y, w, h, speed):
        super().__init__("plane.png", x, y, w, h, speed)
    def move(self):
        self.x += self.speed
    def render(self, gamepad):
        gamepad.blit(self.img, (self.x , self.y))
    def collision(self, enemy):
        self.left = enemy.x
        self.right = enemy.x + enemy.w
        self.top = enemy.y
        self.bottom = enemy.y + enemy .h
        # print(self.left , " ," , self.right , "," , self.top , " ," , self.bottom)
        # print(self.x ,",", self.y)
        if self.x >= self.left:
            print(self.x)
            print(self.left)
            return True
        return False
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
            self.bullets.append(Bullet(self.x, self.y, 50, 30, 1))
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

class BG(ImgBase):
    def __init__(self,  x, y, w, h, speed):
        super().__init__("bg.png", x, y, w, h, speed)
    def move(self):
        self.x -= self.speed
        if self.x <= -740:  # 배경이 화면을 다지나가면 뒤로 돌아간다
            self.x = 740
    def render(self, gamepad):
        gamepad.blit(self.img , (self.x , self.y))

def runGame():
    pad_color = (255, 255, 0)
    pad_w = 700
    pad_h = 300
    pad_wh = (pad_w,pad_h)
    gamepad = pygame.display.set_mode(pad_wh)
    pygame.display.set_caption("플라잉게임")
    clock = pygame.time.Clock()
    # ============================= init(초기화) =================================
    bg1 = BG(0, 0, 740, 300, 1)
    bg2 = BG(740, 0, 740, 300, 1)
    em = []
    e1 = Enemy(500, 0, 100, 50, 3)
    em.append(e1)
    p1 = Player(0, 0, 100, 50, 5)
    # ============================================================================
    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # ============================= key (이벤트) =============================
            if event.type == pygame.KEYDOWN:
                p1.keyDown(event.key)
            if event.type == pygame.KEYUP:
                p1.keyUp(event.key)
        # ============================= update(연산) =============================
        # e1.move()
        bg1.move()
        bg2.move()
        p1.move()

        for bullet in p1.bullets:
            bullet.move()
            for e1 in em:
                if bullet.collision(e1):
                    p1.bullets.remove(bullet)
                    em.remove(e1)
        # ============================= render(그리기) ===========================
        gamepad.fill(pad_color)

        bg1.render(gamepad)
        bg2.render(gamepad)
        p1.render(gamepad)
        for e1 in em:
            e1.render(gamepad)
        for bullet in p1.bullets:
            bullet.render(gamepad)

        # ========================================================================
        pygame.display.update()  # 화면지우기
        clock.tick(60)  # 화면을 60프레임 으로 고정
pygame.init()  # 초기화
runGame()      # 실행
pygame.quit()  # 해제
