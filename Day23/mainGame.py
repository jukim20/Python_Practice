import pygame


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
