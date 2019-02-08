import pygame
import random
from Day25_Platform.settings import*
from Day25_Platform.sprite import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH ,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        p1 = Platform(0, HEIGHT - 40, WIDTH, 40)
        p2 = Platform(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)
        self.platforms.add(p1)
        self.platforms.add(p2)
        self.all_sprites.add(p1)
        self.all_sprites.add(p2)
        self.all_sprites.add(self.player)

        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        if self.player.pos.y > 0:
            hits = pg.sprite.\
                spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        pygame.display.flip()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()