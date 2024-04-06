import pygame
import sys
from src.minigame import run_minigame 

pygame.init()
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Game Window")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
DIALOGUE_BOX_COLOR = WHITE
DIALOGUE_BOX_HEIGHT = 200
DIALOGUE_TEXT_COLOR = BLACK
AVATAR_SIZE = (150, 150)
BORDER_THICKNESS = 5
GRAY = (128, 128, 128)
background_image = pygame.image.load('assets/images/sky.png').convert_alpha()
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
personnage_avatar = pygame.image.load('assets/images/player.png').convert_alpha()
personnage_avatar = pygame.transform.scale(personnage_avatar, AVATAR_SIZE)
dieu_avatar = pygame.image.load('assets/images/god.png').convert_alpha()
dieu_avatar = pygame.transform.scale(dieu_avatar, AVATAR_SIZE)
hoppy_avatar = pygame.image.load('assets/images/groppy.png').convert_alpha()
hoppy_avatar = pygame.transform.scale(hoppy_avatar, AVATAR_SIZE)

dialogues = [
    ("Personnage", "Comment je suis arrivé ici ??", personnage_avatar, 'assets/images/sky.png'),
    ("Dieu", "Hola jeune chico tu n'as pas assez accès au paradis car toute ta vie tu t'es concentré sur toi même ...", dieu_avatar, 'assets/images/sky.png'),
    ("Dieu", "Tu n'as pas assez 'OUVERT' ton esprit durant ta misérable vie de mauvais nullos.", dieu_avatar, 'assets/images/sky.png'),
    ("Personnage", "Ce n'est pas que je suis égoïste, mais je n'aime pas partager avec les gueux de ce monde !!!!", personnage_avatar, 'assets/images/sky.png'),
    ("Dieu", "T'as pas de taff, t'as pas de meuf, t'as pas de thune. T'es qu'une personne pour qui je n'ai pas de respect.", dieu_avatar, 'assets/images/sky.png'),
    ("Dieu", "Mais la grande personne que je suis (humble)", dieu_avatar, 'assets/images/sky.png'),
    ("Dieu", "Te laisse une chance de te racheter et de venir au paradis pour ...", dieu_avatar, 'assets/images/sky.png'),
    ("Dieu", "Avoir de la co.. et des pu.. .. Enfin Bref Bonne chance", dieu_avatar, 'assets/images/sky.png'),
    ("Personnage", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH je suis choqué de ouf la (tombe du paradis).", personnage_avatar, 'assets/images/fall.png'),
    ("Personnage", "Ouille ça fait mal de tomber de si haut", personnage_avatar, 'assets/images/street_blur.png'),
    ("Hoppy", "Miou miouu mioumiou miou miaou miou myyu mou miooou ?", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Mmmh mmh (tousse)", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Désolé mauvais langage mauvaise habitude que j'ai prise là où je traine", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Je me présente Hoppy un chat ....", hoppy_avatar, 'assets/images/street.png'),
    ("Personnage", "Juste un chat ... c'est tout ... un chat ..", personnage_avatar, 'assets/images/street.png'),
    ("Personnage", "Décevant ..", personnage_avatar, 'assets/images/street.png'),
    ("Hoppy", "Alors je ne suis pas qu'un chat, je suis le serviteur de Dieu", hoppy_avatar, 'assets/images/street.png'),
    ("Personnage", "Toi serviteur de Dieu .. Je n'y crois pas", personnage_avatar, 'assets/images/street.png'),
    ("Hoppy", "M'en fous", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Je suis là pour t'aider à revenir au paradis une fois que tu auras plus ouvert ton esprit sur le monde", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Pour cela je vais te proposer des défis à réaliser pour devenir une meilleure personne.", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Tiens voici les défis que je te propose, sachant que tu n'es pas obligé de tous les faire.", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Il te suffit de remplir la jauge du Partage et de l'amitié", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "NE LA VIDE PAS OU TU MOURRAS", hoppy_avatar, 'assets/images/street.png'),
    ("Personnage", "Okééé", personnage_avatar, 'assets/images/street.png'),
]

dialogue_index = 0
font = pygame.font.SysFont('Arial', 22)

def draw_text(text, position, avatar):
    if avatar:
        screen.blit(avatar, (60, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 35))
    text_surface = font.render(text, True, DIALOGUE_TEXT_COLOR)
    screen.blit(text_surface, position)

def draw_dialogue_box():
    pygame.draw.rect(screen, BROWN, pygame.Rect(0, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT - BORDER_THICKNESS,
                                                 WINDOW_WIDTH, DIALOGUE_BOX_HEIGHT + (2 * BORDER_THICKNESS)))
    pygame.draw.rect(screen, DIALOGUE_BOX_COLOR, pygame.Rect(0, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT,
                                                             WINDOW_WIDTH, DIALOGUE_BOX_HEIGHT))

def draw_pause_menu():
    blur_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    blur_surface.set_alpha(100)
    blur_surface.fill(BLACK)
    screen.blit(blur_surface, (0, 0))
    pause_menu_rect = pygame.Rect(WINDOW_WIDTH // 4, WINDOW_HEIGHT // 4, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    pygame.draw.rect(screen, GRAY, pause_menu_rect)
    pygame.draw.rect(screen, BLACK, pause_menu_rect, BORDER_THICKNESS)
    continue_text = font.render("Continuer", True, BLACK)
    continue_rect = continue_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
    screen.blit(continue_text, continue_rect)
    quit_text = font.render("Quitter", True, BLACK)
    quit_rect = quit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
    screen.blit(quit_text, quit_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if continue_rect.collidepoint(mouse_pos):
                return False
            elif quit_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
    return True

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
        if dialogue_index < len(dialogues):
            _, _, _, background_path = dialogues[dialogue_index]
            local_background_image = pygame.image.load(background_path).convert_alpha()
            local_background_image = pygame.transform.scale(local_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
            screen.blit(local_background_image, (0, 0))
            draw_dialogue_box()
            speaker, dialogue, avatar, _ = dialogues[dialogue_index]
            draw_text(f"{speaker}: {dialogue}", (220, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 60), avatar)
        else:
            screen.blit(background_image, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

def main():
    pygame.init()
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Game Window")
    font = pygame.font.SysFont('Arial', 22)
    intro_scene()
    score = 0
    while score < 50:
        score = run_minigame(screen, font)

if __name__ == "__main__":
    main()