import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVEMT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self,*a):
        self.rect.y += self.speed

class Backgroup(GameSprite):
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
class Enemy(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/images/enemy1.png')
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    def __del__(self):
        print('敌机死拉%s'%self.rect)
class Hero(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/images/life.png',0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y -20
        bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)
        pygame.display.update()
class Hero_two(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/images/life.png',0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullet_two = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire_two(self):
        bullet_two = Bullet_two()
        bullet_two.rect.bottom = self.rect.y -20
        bullet_two.rect.centerx = self.rect.centerx
        self.bullet_two.add(bullet_two)
class Bullet(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/images/bullet1.png',-2)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
class Bullet_two(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/images/bullet2.png',-2)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
