import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
background = pygame.image.load("bg_blue.png")
pygame.mouse.set_visible(False)

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("gunshot.wav")

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]





crosshair = Crosshair("target_colored.png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


target_group = pygame.sprite.Group()

for target in range(20):
    new_target = Target("duck_brown.png", random.randrange(0, 800), random.randrange(0, 800))
    target_group.add(new_target)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
