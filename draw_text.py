import pygame.font


def text(text, font_name, size, color):
    font = pygame.font.Font(f'game_files/fonts/{font_name}', size)
    return font.render(text, True, color)
