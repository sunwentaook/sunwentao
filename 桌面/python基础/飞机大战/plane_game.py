import pygame
from plane_sprites import *
class PlaneGame(object):
    def __init__(self):
        print('游戏初始化')
        # 1.创建游戏窗口 pygame.display.set_mode 需要创建窗口的款和高
        # .size是去宽高 .x是去x轴的值 .y是去y轴的值
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟 pygame.time.Clock() 会给我们传入一个时钟对象
        self.clock = pygame.time.Clock()
        # 3.调用私有方法 里面创建精灵和精灵组
        self.__create_sprite()
        # 4.设置定时器事件 每秒创建一架敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        # 5.每隔0.5秒发射一个子弹
        pygame.time.set_timer(HERO_FIRE_EVENT,200)
    def start_game(self):
        while True:
            # 1.设置帧率
            self.clock.tick(60)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新精灵组
            self.__update_sprites()
            # 5.更新屏幕显示
            pygame.display.update()

    def __create_sprite(self):
        '''创建精灵组'''
        # pygame.sprite.Group() 可以创建一个精灵组
        # 1.精灵组
        bg1 = BackGroup('/home/sunwentao/桌面/python基础/images/background.png')
        bg2 = BackGroup('/home/sunwentao/桌面/python基础/images/background.png')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 2.敌机组
        self.enemy_group = pygame.sprite.Group()
        # 3.英雄组
        bg3 = Hero('/home/sunwentao/桌面/python基础/images/me1.png')
        bg4 = Hero('/home/sunwentao/桌面/python基础/images/me1.png')
        bg3.rect.x = -bg4.rect.width
        self.hero_group = pygame.sprite.Group(bg3,bg4)

    def __event_handler(self):
        '''事件监听的方法'''
        # pygame.event.get() 获取监听事件的列表
        # 获取玩列表以后 用for循环 循环这个列表
        for event in pygame.event.get():
        # 
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type ==CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed = 4
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -4
            else:
                self.hero.speed = 0
    def __check_collide(self):
        '''碰撞检测的方法'''
        # 1.子弹摧毁飞机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        # 2.英雄撞到敌机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        # 3.判断列表时候有内容
        if len(enemies)>0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()
    def __update_sprites(self):
        '''更新精灵组的方法'''
        for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
        # 更新精灵组里面所有精良的位置
            group.update()
            # 绘制到屏幕上
            group.draw(self.screen)
    @staticmethod
    def __game_over():
        '''游戏结束的方法'''
        print('游戏结束')
        pygame.quit()
        exit()





if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
