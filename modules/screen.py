import pygame
import modules.path_to_file as m_path



screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Battle Ship")

pygame.display.set_icon(pygame.image.load(m_path.find_path_to_file("img/1.ico")))
#А пон у меня вылетело щас