import pygame
import random
from Day18.cMyRect01 import *

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000, 800))
r1 = MyRect()
r1.set_info((255, 0, 0), (0, 0), (50, 50))
r2 = MyRect()
r2.set_info((255, 255, 0), (0, 80), (50, 50))

r_list = []  # 담아서 관리해야됨
r_list.append(r1)
r_list.append(r2)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                r_list[0].isUp = True
            if event.key == pygame.K_DOWN:
                r_list[0].isDown = True
            if event.key == pygame.K_RIGHT:
                r_list[0].isRight = True
            if event.key == pygame.K_LEFT:
                r_list[0].isLeft = True
            if event.key == pygame.K_a:
                r_list[1].isLeft = True
            if event.key == pygame.K_d:
                r_list[1].isRight = True
            if event.key == pygame.K_s:
                r_list[1].isDown = True
            if event.key == pygame.K_w:
                r_list[1].isUp = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                r_list[0].isUp = False
            if event.key == pygame.K_DOWN:
                r_list[0].isDown = False
            if event.key == pygame.K_RIGHT:
                r_list[0].isRight = False
            if event.key == pygame.K_LEFT:
                r_list[0].isLeft = False
            if event.key == pygame.K_a:
                r_list[1].isLeft = False
            if event.key == pygame.K_d:
                r_list[1].isRight = False
            if event.key == pygame.K_s:
                r_list[1].isDown = False
            if event.key == pygame.K_w:
                r_list[1].isUp = False

        r_list[0].keyManager(event)
    # ===============================================
    for rect in r_list:
        rect.update()
    for bullet in r_list[0].bulletList:
        bullet.update()

    screen.fill((255, 255, 255))  # 잔상이 남게 하지 않으려면 배경을 지워줘야한다
    for rect in r_list:
        pygame.draw.rect(screen, rect.color, pygame.Rect((rect.x, rect.y), rect.size))

    for bullet in r_list[0].bulletList:
        pygame.draw.rect(screen, bullet.color, pygame.Rect((bullet.x, bullet.y), bullet.size))

    # 문제 1) 플레이어는 위 아래 움직인다 스페이스를 누르면 총알 발사 총알은 벽에 닿으면 구석에 정지
    # 문제 2) ai
    # 문제 2) asdw 노란색을 조정하고 방향키는 빨간색 조종

    # ===============================================
    pygame.display.flip()
    clock.tick(60)
pygame.quit()