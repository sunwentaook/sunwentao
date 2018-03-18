import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
class GameSprites(pygame.sprite.Sprite):
    def __init__(self,image_url,speed=1):
        super().__init__()
        self.image_url = pygame.image.load(image_url)
        self.speed = speed
        self.rect = self.image_url.get_rect()
    def update(self):
        self.rect.y += self.speed
class Hero(GameSprites):
    def __init__(self,image_url,speed=0):
        super().__init__(image_url,speed)
    def update(self):
        pass
class Backgroup(GameSprites):
    def __init__(self,image_url,speed=1):
        super().__init__(image_url)
    def update(self):
        pass
