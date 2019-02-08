import pygame

# file ==> settings ==> Project : workspace ==> project interpreter ==> + ==> pygame
# 1. 프레임 (60) 초당 60번 돌아간다는 뜻
# 2. 윈도창 (x, y)
# 3. 이벤트 (마우스 , 키보드 , 사운드 등등)

pygame.init()  # 초기화
size_x = 1200
size_y = 800

screen = pygame.display.set_mode((size_x, size_y))  # 윈도우 생성
end = False

r = 255
g = 255
b = 255
isRed = False
clock = pygame.time.Clock()  # 파이게임에서 제공하는 시간

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x 버튼을 눌러 창을 닫는 것
            end = True

        # ====================== key setting ====================
        if event.type == pygame.KEYDOWN:  # (대전재) 키가 눌렸을 때 ==> 어떤 키냐?
            if event.key == pygame.K_1:  # 그 키가 숫자 1 이라면
                isRed = True
                # r -= 120
                # if r < 0:
                #     r = 255
            if event.key == pygame.K_a:  # 그 키가 a 라면
                g -= 20
                if g < 0:
                    g = 255
            if event.key == pygame.K_DOWN:
                b -= 20
                if b < 0:
                    b = 255
        elif event.type == pygame.KEYUP:  # (대전재) 키가 띄어졌을 때 ==> 어떤 키냐?
            if event.key == pygame.K_1:
                isRed = False
                # r += 120

        # 파이썬의 단점: 멀티키가 안 됨 (두 키를 함께 입력할 수 없음)

        # ===========================================================
        if isRed:
            r -= 2
    # ===========================================================

    screen.fill((r, g, b))  # 배경색 변경
    pygame.display.flip()  # while 문 속에서 화면을 지우고 다시 그리고를 반복
    clock.tick(60)  # 초당 60 프레임

pygame.quit()  # 종료

