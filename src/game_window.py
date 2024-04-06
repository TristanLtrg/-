import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
DIALOGUE_BOX_COLOR = WHITE
DIALOGUE_BOX_HEIGHT = 200
DIALOGUE_TEXT_COLOR = BLACK
AVATAR_SIZE = (150, 150)
BORDER_THICKNESS = 5

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

background_image = pygame.image.load('assets/images/sky.png').convert_alpha()
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
personnage_avatar = pygame.image.load('assets/images/player.png').convert_alpha()
personnage_avatar = pygame.transform.scale(personnage_avatar, AVATAR_SIZE)
dieu_avatar = pygame.image.load('assets/images/god.png').convert_alpha()
dieu_avatar = pygame.transform.scale(dieu_avatar, AVATAR_SIZE)

dialogues = [
    ("Personnage", "Bonjour, pourquoi m'avez-vous convoquez ici ?", personnage_avatar),
    ("Dieu", "Désolé de te l'annoncé mais tu es viré du domaine céleste.", dieu_avatar),
    ("Personnage", "Comment ça ? comment est-ce possible ?", personnage_avatar),
    ("Dieu", "T'as pas de taff, t'as pas de meuf, t'as pas de thune. T'es qu'une personne pour qui je n'ai pas de respect.", dieu_avatar)
]
dialogue_index = 0

font = pygame.font.SysFont('Arial', 24)

def draw_text(text, position, avatar=None):
    if avatar:
        screen.blit(avatar, (60, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 35))
    text_surface = font.render(text, True, DIALOGUE_TEXT_COLOR)
    screen.blit(text_surface, position)

def draw_dialogue_box():
    pygame.draw.rect(screen, BROWN, pygame.Rect(0, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT - BORDER_THICKNESS,
                                                 WINDOW_WIDTH, DIALOGUE_BOX_HEIGHT + (2 * BORDER_THICKNESS)))
    pygame.draw.rect(screen, DIALOGUE_BOX_COLOR, pygame.Rect(0, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT,
                                                             WINDOW_WIDTH, DIALOGUE_BOX_HEIGHT))

def intro_scene():
    global dialogue_index
    intro_done = False
    while not intro_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues):
                        intro_done = True

        screen.blit(background_image, (0, 0))
        draw_dialogue_box()

        if dialogue_index < len(dialogues):
            speaker, dialogue, avatar = dialogues[dialogue_index]
            draw_text(f"{speaker}: {dialogue}", (220, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 60), avatar)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

def main_game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BLACK)
        #FAire le BIg Jeu ICi

        pygame.display.flip()

if __name__ == "__main__":
    intro_scene()
    main_game()
    pygame.quit()
