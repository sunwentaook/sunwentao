import pygame
from plane_sprites import *
class GameSprites(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,300)
    def start_game(self):
        '''开始游戏'''
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    def __create_sprites(self):
        '''精灵组'''
        bg1 = Backgroup('/home/sunwentao/桌面/python基础/images/background.png')
        bg2 = Backgroup('/home/sunwentao/桌面/python基础/images/background.png')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        self.hero = Hero()
        self.hero_two = Hero_two()
        self.hero_group = pygame.sprite.Group(self.hero,self.hero_two)
        self.enemy_group =pygame.sprite.Group()
    def __event_handler(self):
        '''事件监听'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed = 4
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -4
            elif key_pressed[pygame.K_UP]:
                self.hero.fire()
            else:
                self.hero.speed = 0
            if key_pressed[pygame.K_d]:
                self.hero_two.speed = 4
            elif key_pressed[pygame.K_a]:
                self.hero_two.speed = -4
            elif key_pressed[pygame.K_SPACE]:
                self.hero_two.fire_two()
            else:
                self.hero_two.speed = 0
    def __check_collide(self):
        '''碰撞检测'''
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies)>0:
            self.hero.kill()
            GameSprites.__game_over()
        pygame.sprite.groupcollide(self.hero_two.bullet_two,self.enemy_group,True,True)
        enemie_two = pygame.sprite.spritecollide(self.hero_two,self.enemy_group,True)
        if len(enemie_two)>0:
            self.hero_two.kill()
            GameSprites.__game_over()
    def __update_sprites(self):
        '''更新精灵组'''
        for group in [self.back_group,self.hero_group,self.enemy_group,self.hero.bullets,self.hero_two.bullet_two]:
            group.update()
            group.draw(self.screen)
        self.hero.bullets.update()
    @staticmethod
    def __game_over():
        '''死亡'''
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = GameSprites()
    game.start_game()
