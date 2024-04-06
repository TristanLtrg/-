import pygame
import sys
from src.game_window import main as start_game

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TEXTS = {
    "start": "Démarrer",
    "settings": "Paramètres",
    "quit": "Quitter",
}

running = True

def draw_main_menu(screen):
    menu_items = [TEXTS["start"], TEXTS["settings"], TEXTS["quit"]]
    return draw_menu(screen, menu_items)

def draw_menu(screen, menu_items):
    menu_font = pygame.font.SysFont(None, 50)
    menu_item_height = 100
    menu_item_width = 200
    menu_item_margin = 20
    menu_x = (WINDOW_WIDTH - menu_item_width) // 2
    menu_y = (WINDOW_HEIGHT - (len(menu_items) * (menu_item_height + menu_item_margin))) // 2

    button_dict = {}

    for i, item in enumerate(menu_items):
        text = menu_font.render(item, True, BLACK)
        button_rect = pygame.Rect(menu_x, menu_y + i * (menu_item_height + menu_item_margin), menu_item_width, menu_item_height)
        pygame.draw.rect(screen, WHITE, button_rect)
        screen.blit(text, (menu_x + (menu_item_width - text.get_width()) // 2, menu_y + i * (menu_item_height + menu_item_margin) + (menu_item_height - text.get_height()) // 2))
        button_dict[item] = button_rect

    return button_dict

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Menu")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                buttons_dict = draw_main_menu(screen)
                if buttons_dict is not None:
                    for item, rect in buttons_dict.items():
                        if rect.collidepoint(mouse_x, mouse_y):
                            if item == "Démarrer":
                                print("Démarrer le jeu")
                                start_game()
                                pygame.quit()
                                sys.exit()
                            elif item == "Quitter":
                                print("Quitter le jeu")
                                pygame.quit()
                                sys.exit()
    screen.fill(WHITE)
    draw_main_menu(screen)
    pygame.display.flip()
pygame.quit()
