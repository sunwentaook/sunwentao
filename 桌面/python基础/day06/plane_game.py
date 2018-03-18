import pygame
from plane_sprites import *
class PlanGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
    def start_game(self):
        while True:
            self.clock.tick(60)
            self.__even_hander()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    def __create_sprites(self):
        bg1 
        self.bg_group = pygame.sprite.Group()
        self.bb_group = pygame.sprite.Group()
        self.yy_group = pygame.sprite.Group()
    def __even_hander(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_over()
#            elif event.type == pygame.K_q:
#                PlanGame.__game_over()
                
    def __check_collide(self):
        pass
    def __update_sprites(self):
        for group in [self.bg_group,self.bb_group,self.yy_group]:
            group.update()
            group.draw(self.screen)
    @staticmethod
    def __game_over():
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = PlanGame()
    game.start_game()


