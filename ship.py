import pygame
import modules.settings as m_settings
# 
class Ship(m_settings.Settings):
    def __init__(self,width1=40,heigt1=40, x1 = 0, y1=0, name_file1= None, rotate1=False, rotate2= False):
        m_settings.Settings.__init__(self,width=width1, height=heigt1, x= x1, y=y1,name_file=name_file1, rotate=rotate1, T_F_rotate=rotate2)
        self.load_image()
        self.SHIP = 1 
        self.ANGLE = "R"
        self.COUNT2 = 0
        self.DAMAGE = 0
        self.CELLS = []
    
ship = Ship(name_file1="img/1.png")
double_ship = Ship(width1=80, heigt1=40, name_file1="img/2.png", x1= 40, y1=0)
triple_ship = Ship(width1=120, heigt1=40, name_file1="img/3.png", x1=120, y1=0)
fourth_ship = Ship(width1=160, heigt1=40, name_file1="img/4.png", x1=240, y1=0)
