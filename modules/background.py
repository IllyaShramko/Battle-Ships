import pygame
import modules.path_to_file as m_path
import modules.screen as screeen
import modules.settings as m_sett


class Back(m_sett.Settings):
    def __init__(self, width1=0, height1=0, x1=0, y1=0, name_file1=None, rotate1=0, T_F_rotate1=False):
        m_sett.Settings.__init__(self=self ,width=width1, height=height1, x=x1, y=y1, name_file=name_file1, rotate=rotate1, T_F_rotate=T_F_rotate1)
        self.load_image()
background = Back(width1=1000,height1=700,x1=0,y1=0,name_file1="img/background.jpg")