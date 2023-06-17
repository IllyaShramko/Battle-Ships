import pygame
import modules.screen as m_screen
pygame.init()


def draw_table(x1, y):
    x = x1
    for i in range(10):
        for i in range(10):
            pygame.draw.rect(
                surface=m_screen.screen,
                color=(0, 100 ,255),
                rect=(x,y,40,40)
            )
            pygame.draw.rect(
                surface=m_screen.screen,
                color=(0, 0, 0),
                rect=(x,y,40,40),
                width=2

            )
            x = x + 40
        x = x1
        y = y + 40
        
