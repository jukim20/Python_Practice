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
isRight = False
isLeft = False
isUp = False
isDown = False
rect_x = size_x/2 - 100
rect_y = size_y/2 - 100
s_rect_x = size_x/2 - 40
s_rect_y = size_y/2 - 40

clock = pygame.time.Clock()  # 파이게임에서 제공하는 시간

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x 버튼을 눌러 창을 닫는 것
            end = True

     # ====================== Key Setting =======================
        if event.type == pygame.KEYDOWN:  # (대전재) 키가 눌렸을 때 ==> 어떤 키냐?
            if event.key == pygame.K_RIGHT:  # 그 키가 숫자 1 이라면
                isRight = True
            elif event.key == pygame.K_LEFT:
                isLeft = True
            elif event.key == pygame.K_UP:
                isUp = True
            elif event.key == pygame.K_DOWN:
                isDown = True

        elif event.type == pygame.KEYUP:  # (대전재) 키가 띄어졌을 때 ==> 어떤 키냐?
            if event.key == pygame.K_RIGHT:
                isRight = False
            elif event.key == pygame.K_LEFT:
                isLeft = False
            elif event.key == pygame.K_UP:
                isUp = False
            elif event.key == pygame.K_DOWN:
                isDown = False

    # ======================= Update ============================

    if isRight:
        rect_x += 5
    if isLeft:
        rect_x -= 5
    if isUp:
        rect_y -= 5
    if isDown:
        rect_y += 5

    if rect_x < s_rect_x:
        s_rect_x = rect_x
    elif rect_x > s_rect_x + 40:
        s_rect_x = rect_x + 40
    if rect_y > s_rect_y:
        s_rect_y = rect_y

    # ======================= Render ============================
    screen.fill((r, g, b))  # 배경색 변경
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((rect_x, rect_y), (200, 200)))  # 위치 , 사이즈

    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect((s_rect_x , s_rect_y), (80, 80)))

    # 윈도우창, 색깔, 렉트 (위치, 사이즈)
    # 가운데 그리기 : 스크린 / 2 - 자기사이즈 / 2

    # ===========================================================
    pygame.display.flip()  # while 문 속에서 화면을 지우고 다시 그리고를 반복
    clock.tick(60)  # 초당 60 프레임

# 문제 1) 조그만 렉트 한 개 추가 (80, 80)
# 문제 2) 큰 렉트를 키로 움직여보자
#

pygame.quit()  # 종료



