import pygame
import modules.path_to_file as m_path
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(m_path.find_path_to_file("music/PON.mp3"))
# pygame.mixer.Sound(m_path.find_path_to_file("music/PON.mp3"))
# pygame.mixer_mu.
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(loops=99999)