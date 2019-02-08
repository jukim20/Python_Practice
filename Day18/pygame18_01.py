import pygame
import random


class MyRect:
    def set_info(self, color, pos, size):
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.size = size

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
r1 = MyRect()
r1.set_info((255, 0, 0), (0, 0), (50, 50))
r2 = MyRect()
r2.set_info((255, 255, 0), (0, 80), (50, 50))
r3 = MyRect()
r3.set_info((0, 255, 0), (0, 160), (50, 50))
r4 = MyRect()
r4.set_info((0, 255, 255), (0, 240), (50, 50))
r5 = MyRect()
r5.set_info((0, 0, 255), (0, 320), (50, 50))

r_list = []  # 담아서 관리해야됨
r_list.append(r1)
r_list.append(r2)
r_list.append(r3)
r_list.append(r4)
r_list.append(r5)

run = True
isStart = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                isStart = True

    # ===============================================
    if isStart:
        for rect in r_list:
            rect.x += random.randint(0, 3)

    screen.fill((255, 255, 255))  # 잔상이 남게 하지 않으려면 배경을 지워줘야한다
    for rect in r_list:
        pygame.draw.rect(screen, rect.color, pygame.Rect((rect.x, rect.y), rect.size))
    # pygame.draw.rect(screen, r1.color, pygame.Rect(r1.pos, r1.size))
    # pygame.draw.rect(screen, r2.color, pygame.Rect(r2.pos, r2.size))

    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((0, 0), (50, 50)))
    # 문제 1) 렉트를 5개 띄우고 버튼을 누르면 경기시작 5명이 랜덤으로 조금씩 오른쪽 이동. 1등을 가리자


    # ===============================================
    pygame.display.flip()
    clock.tick(60)
pygame.quit()