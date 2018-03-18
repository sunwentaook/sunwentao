import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,700,480)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVEMT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self,*a):
        self.rect.x += self.speed
class Backgroup(GameSprite):
    def update(self):
        super().update()
        if self.rect.x >=SCREEN_RECT.width:
            self.rect.x = -self.rect.width
class Enemy(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/enemy1.png')
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.height -self.rect.height
        self.rect.y = random.randint(0,max_x)
    def update(self):
        super().update()
        if self.rect.x >= SCREEN_RECT.width:
            self.kill()
    def __del__(self):
        print('敌机死啦')
class Hero(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/me1.png',0)
        self.rect.x = SCREEN_RECT.x
        self.rect.x = SCREEN_RECT.x +574
        self.bullets = pygame.sprite.Group()
    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 57:
            self.rect.top = 57
        if self.rect.bottom > 423:
            self.rect.bottom = 423
    def fire(self):
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.y = self.rect.y + i*45
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)
            pygame.display.update()
class Hero_two(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/me2.png',0)
        self.rect.x = SCREEN_RECT.x
        self.rect.x = SCREEN_RECT.x +574
        self.bullet_two = pygame.sprite.Group()
        self.hero_liao = pygame.sprite.Group()
    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 57:
            self.rect.top = 57
        if self.rect.bottom > 423:
            self.rect.bottom = 423
    def fire_two(self):
        for i in (0,1,2):
            bullet_two = Bullet_two()
            bullet_two.rect.y = self.rect.y + i*45
            bullet_two.rect.centerx = self.rect.centerx
            self.bullet_two.add(bullet_two)
            pygame.display.update()

class Hero1(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/life.png',0)
        self.rect.x = SCREEN_RECT.x
        self.rect.x = SCREEN_RECT.x +654
        self.bullet1 = pygame.sprite.Group()
    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 323:
            self.rect.bottom = 323
    def fire1(self):
        bullet1 = Bullet()
        bullet1.rect.y = self.rect.y +29
        bullet1.rect.centerx = self.rect.centerx
        self.bullet1.add(bullet1)
        pygame.display.update()
class Hero2(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/life.png',0)
        self.rect.x = SCREEN_RECT.x
        self.rect.x = SCREEN_RECT.x +654
        self.bullet2 = pygame.sprite.Group()
    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 154:
            self.rect.top = 154
        if self.rect.bottom > 480:
            self.rect.bottom = 480
    def fire2(self):
        bullet2 = Bullet()
        bullet2.rect.y = self.rect.y +29
        bullet2.rect.centerx = self.rect.centerx
        self.bullet2.add(bullet2)
        pygame.display.update()
class Hero3(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/life.png',0)
        self.rect.x = SCREEN_RECT.x
        self.rect.x = SCREEN_RECT.x +654
        self.bullet3 = pygame.sprite.Group()
    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 323:
            self.rect.bottom = 323
    def fire3(self):
        bullet3 = Bullet_two()
        bullet3.rect.y = self.rect.y +29
        bullet3.rect.centerx = self.rect.centerx
        self.bullet3.add(bullet3)
        pygame.display.update()
class Hero4(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/life.png',0)
        self.rect.x = SCREEN_RECT.x
        self.rect.x = SCREEN_RECT.x +654
        self.bullet4 = pygame.sprite.Group()
    def update(self):
        self.rect.y += self.speed
        if self.rect.top < 154:
            self.rect.top = 154
        if self.rect.bottom > 480:
            self.rect.bottom = 480
    def fire4(self):
        bullet4 = Bullet_two()
        bullet4.rect.y = self.rect.y +29
        bullet4.rect.centerx = self.rect.centerx
        self.bullet4.add(bullet4)
        pygame.display.update()
class Bullet(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/bullet1.png',-2)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
class Bullet_two(GameSprite):
    def __init__(self):
        super().__init__('/home/sunwentao/桌面/python基础/image2/bullet2.png',-2)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
