import pygame
from plane_sprites import *
class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprite()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,2000)
    def start_game(self):
        '''开始游戏'''
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    def __create_sprite(self):
        '''精灵组'''
        bg1 = Backgroup('/home/sunwentao/桌面/python基础/image2/background.png')
        bg2 = Backgroup('/home/sunwentao/桌面/python基础/image2/background.png')
        bg2.rect.x = -bg2.rect.width
        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_two = Hero_two()
        self.hero1 = Hero1()
        self.hero2 = Hero2()
        self.hero3 = Hero3()
        self.hero4 = Hero4()
        self.hero_group = pygame.sprite.Group(self.hero,self.hero_two,self.hero1,self.hero2,self.hero3,self.hero4)
    def __event_handler(self):
        '''事件监听'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_DOWN]:
                self.hero.speed = 4
            elif key_pressed[pygame.K_UP]:
                self.hero.speed = -4
            elif key_pressed[pygame.K_LEFT]:
                self.hero.fire()
            else:
                self.hero.speed = 0
            if key_pressed[pygame.K_DOWN]:
                self.hero1.speed = 4
            elif key_pressed[pygame.K_UP]:
                self.hero1.speed = -4
            elif key_pressed[pygame.K_LEFT]:
                self.hero1.fire1()
            else:
                self.hero1.speed = 0
            if key_pressed[pygame.K_DOWN]:
                self.hero2.speed = 4
            elif key_pressed[pygame.K_UP]:
                self.hero2.speed = -4
            elif key_pressed[pygame.K_LEFT]:
                self.hero2.fire2()
            else:
                self.hero2.speed = 0
            if key_pressed[pygame.K_s]:
                self.hero_two.speed = 4
            elif key_pressed[pygame.K_w]:
                self.hero_two.speed = -4
            elif key_pressed[pygame.K_a]:
                self.hero_two.fire_two()
            else:
                self.hero_two.speed = 0
            if key_pressed[pygame.K_s]:
                self.hero3.speed = 4
            elif key_pressed[pygame.K_w]:
                self.hero3.speed = -4
            elif key_pressed[pygame.K_a]:
                self.hero3.fire3()
            else:
                self.hero3.speed = 0
            if key_pressed[pygame.K_s]:
                self.hero4.speed = 4
            elif key_pressed[pygame.K_w]:
                self.hero4.speed = -4
            elif key_pressed[pygame.K_a]:
                self.hero4.fire4()
            else:
                self.hero4.speed = 0
    def __check_collide(self):
        '''碰撞检测'''
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        pygame.sprite.groupcollide(self.hero_two.bullet_two,self.enemy_group,True,True)
        enemie_two = pygame.sprite.spritecollide(self.hero_two,self.enemy_group,True)
        pygame.sprite.groupcollide(self.hero1.bullet1,self.enemy_group,True,True)
        pygame.sprite.groupcollide(self.hero2.bullet2,self.enemy_group,True,True)
        pygame.sprite.groupcollide(self.hero3.bullet3,self.enemy_group,True,True)
        pygame.sprite.groupcollide(self.hero4.bullet4,self.enemy_group,True,True)
        enemie1 = pygame.sprite.spritecollide(self.hero1,self.enemy_group,True)
        enemie2 = pygame.sprite.spritecollide(self.hero2,self.enemy_group,True)
        enemie3 = pygame.sprite.spritecollide(self.hero3,self.enemy_group,True)
        enemie4 = pygame.sprite.spritecollide(self.hero4,self.enemy_group,True)
        if len(enemies)>0:
            self.hero.kill()
            self.hero1.kill()
            self.hero2.kill()
            PlaneGame.__game_over()
        elif len(enemie_two)>0:
            self.hero_two.kill()
            self.hero3.kill()
            self.hero4.kill()
            PlaneGame.__game_over()
        elif len(enemie1)>0:
            self.hero1.kill()
        elif len(enemie2)>0:
            self.hero2.kill()
        elif len(enemie3)>0:
            self.hero3.kill()
        elif len(enemie4)>0:
            self.hero4.kill()
    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.hero_group,self.enemy_group,self.hero.bullets,self.hero_two.bullet_two,self.hero1.bullet1,self.hero2.bullet2,self.hero3.bullet3,self.hero4.bullet4]:
            group.update()
            group.draw(self.screen)
        self.hero.bullets.update()
        self.hero1.bullet1.update()
        self.hero2.bullet2.update()
        self.hero3.bullet3.update()
        self.hero4.bullet4.update()
    @staticmethod
    def __game_over():
        '''游戏结束'''
        print('游戏结束')
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
