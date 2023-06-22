import pygame
import modules.screen as m_screen
import modules.data as m_data

pygame.init()
def draw_menu():
    color = (0, 0, 0)
    if m_data.language == "EN":
        font1 = pygame.font.SysFont('comicsansms',70)
        m_screen.screen.blit(font1.render("Play",0,color), (435, 110))
    elif m_data.language == "UA":
        font1 = pygame.font.SysFont('comicsansms',60)
        m_screen.screen.blit(font1.render("Грати",0,color), (415, 116))
    
    if m_data.language == "EN":
        font1 = pygame.font.SysFont('comicsansms',40)
        m_screen.screen.blit(font1.render("Language",0,color), (415, 288))
    elif m_data.language == "UA":
        font1 = pygame.font.SysFont('comicsansms',70)
        m_screen.screen.blit(font1.render("Мова",0,color), (412, 267))
    
    if m_data.language == "EN":
        font1 = pygame.font.SysFont('comicsansms',70)
        m_screen.screen.blit(font1.render("Exit",0,color), (425, 425))
    elif m_data.language == "UA":
        font1 = pygame.font.SysFont('comicsansms',65)
        m_screen.screen.blit(font1.render("Вихід",0,color), (410, 425))
    pygame.draw.rect(
        surface=m_screen.screen,
        color=(0,0,0),
        rect=(400,100,200,135),
        width=10,
        border_radius=5
    )
    
    
    pygame.draw.rect(
        surface=m_screen.screen,
        color=(0,0,0),
        rect=(400,255,200,135),
        width=10,
        border_radius=5
    )
    pygame.draw.rect(
        surface=m_screen.screen,
        color=(0,0,0),
        rect=(400,410,200,135),
        width=10,
        border_radius=5
    )
    