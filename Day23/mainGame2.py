import pygame
import random
class Enemy:
    def __init__(self, x, y, w, h, speed):
        self.img = pygame.image.load("bat.png")
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
class Player:
    def __init__(self, x, y, w, h, speed):
        self.img = pygame.image.load("plane.png")
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
class BG:
    def __init__(self, x, y, w, h, speed):
        self.img = pygame.image.load("bg.png")
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
def runGame():
    pad_color = (255, 255, 0)
    pad_w = 1800
    pad_h = 600
    pad_wh = (pad_w,pad_h)
    gamepad = pygame.display.set_mode(pad_wh)
    pygame.display.set_caption("플라잉게임")
    clock = pygame.time.Clock()
    # ============================= init(초기화) =================================
    p1 = Player(0, 0, 100, 50, 5)
    e1 = Enemy(500, 500, 100, 50, 3)
    bg1 = BG(0, 0, 740, 300, 1)
    bg2 = BG(740, 0, 740, 300, 1)
    # ============================================================================
    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # ============================= key (이벤트) =============================

        # ============================= update(연산) =============================
        e1.x -= e1.speed
        if e1.x <= 0:
            e1.x = 800
            e1.y = random.randint(0, 600)
        bg1.x -= bg1.speed
        bg2.x -= bg2.speed
        # ============================= render(그리기) ===========================
        gamepad.fill(pad_color)
        gamepad.blit(bg1.img, (bg1.x, bg1.y))
        gamepad.blit(bg2.img, (bg2.x, bg2.y))
        gamepad.blit(p1.img, (p1.x, p1.y))
        gamepad.blit(e1.img, (e1.x, e1.y))
        # ========================================================================
        pygame.display.update()  # 화면지우기
        clock.tick(60)  # 화면을 60프레임 으로 고정
pygame.init()  # 초기화
runGame()      # 실행
pygame.quit()  # 해제
