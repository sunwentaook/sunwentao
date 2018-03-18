import pygame
from planesprites import *
class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__creat_sprites()
    def start_game(self):
        print('开始游戏')
        while True:
            self.clock.tick(60)
            self.__event_hander()
            self.__update_sprites()
            pygame.display.update()
    def __creat_sprites(self):
        bg1 = Backgroup('/home/sunwentao/桌面/python基础/images/background.png')
        bg2 = Backgroup('/home/sunwentao/桌面/python基础/images/background.png')
        bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2,)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group()
    def __event_hander(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
        
    def __check_collide(self):
        pass
    def __update_sprites(self):
        for group in [self.back_group,self.enemy_group,self.hero_group]:
            group.update()
            group.draw(self.screen)
    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
