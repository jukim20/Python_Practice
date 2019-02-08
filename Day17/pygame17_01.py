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
clock = pygame.time.Clock()  # 파이게임에서 제공하는 시간

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x 버튼을 눌러 창을 닫는 것
            end = True

    # ===========================================================
    r -= 1
    if r == 0:
        r = 255
    # size_x -= 1
    # screen = pygame.display.set_mode((size_x, size_y))

    # ===========================================================

    screen.fill((r, g, b))  # 배경색 변경
    pygame.display.flip()  # while 문 속에서 화면을 지우고 다시 그리고를 반복
    clock.tick(60)  # 초당 60 프레임

pygame.quit()  # 종료

