import pygame  # 60프레임 , x  y  , 이벤트처리
import random
from Day18.cMyRect01 import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
r1 = MyRect()
r1.set_info((255, 0, 0), (0, 0), (50, 50))
r2 = MyRect()
r2.set_info((255, 255, 0), (0, 80), (50, 50))
r_list = []
r_list.append(r1)
r_list.append(r2)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        r_list[0].keyManager(event)  # 1
    # ===============================================
    r_list[0].update()  # 2
    for bullet in r_list[0].bulletList:
        bullet.update()
    screen.fill((255, 255, 255))  # 배경 색지정
    for rect in r_list:  # 3
        pygame.draw.rect(screen, rect.color, pygame.Rect((rect.x, rect.y), rect.size))
    for bullet in r_list[0].bulletList:
        pygame.draw.rect(screen, bullet.color, pygame.Rect((bullet.x, bullet.y), bullet.size))
    # ===============================================
    pygame.display.flip()
    clock.tick(60)
pygame.quit()