import pygame
import modules.path_to_file as m_path
# import modules.brick as m_brick

pygame.init()
# --->
#
#
#
class Settings:
    def __init__(self, width = 0, height= 0, x= 0, y= 0, name_file= None, rotate=0, T_F_rotate=False):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_FILE = name_file
        self.IMAGE = None
        self.ROTATE = rotate
        self.T_F_ROTATE = T_F_rotate
    def load_image(self, check_img = True):
        image1 = pygame.image.load(m_path.find_path_to_file(self.NAME_FILE))
        image1 = pygame.transform.scale(image1, (self.WIDTH, self.HEIGHT))
        if self.T_F_ROTATE or 1:
            if check_img:
                self.IMAGE = pygame.transform.rotate(image1,angle=self.ROTATE)
            else:
                return pygame.transform.rotate(image1,angle=self.ROTATE)
        else:
            self.IMAGE = image1

    def blit_sprite(self, screen_game):
        screen_game.blit(self.IMAGE, (self.X, self.Y))