import pygame
import sys
import random
from src.minigame import run_minigame 

pygame.init()
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("JAM")
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
dieu_avatar_rigole = pygame.image.load('assets/images/god_Laughing.png').convert_alpha()
dieu_avatar_rigole = pygame.transform.scale(dieu_avatar_rigole, AVATAR_SIZE)
hoppy_avatar = pygame.image.load('assets/images/groppy.png').convert_alpha()
hoppy_avatar = pygame.transform.scale(hoppy_avatar, AVATAR_SIZE)

dialogues_intro = [
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
    ("un chat étrange", "Miou miouu mioumiou miou miaou miou myyu mou miooou ?", hoppy_avatar, 'assets/images/street.png'),
    ("un chat", "Mmmh mmh (tousse)", hoppy_avatar, 'assets/images/street.png'),
    ("un chat", "Désolé mauvais langage mauvaise habitude que j'ai prise là où je traine", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Je me présente Hoppy un chat ....", hoppy_avatar, 'assets/images/street.png'),
    ("Personnage", "Juste un chat ... c'est tout ... un chat ..", personnage_avatar, 'assets/images/street.png'),
    ("Personnage", "Décevant ..", personnage_avatar, 'assets/images/street.png'),
    ("Hoppy", "Alors je ne suis pas qu'un chat, je suis le serviteur de Dieu", hoppy_avatar, 'assets/images/street.png'),
    ("Personnage", "Toi serviteur de Dieu .. Je n'y crois pas", personnage_avatar, 'assets/images/street.png'),
    ("Hoppy", "M'en fous", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Je suis là pour t'aider à revenir au paradis une fois que tu auras plus ouvert ton esprit sur le monde", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Pour cela je vais te proposer une série de défis à réaliser pour devenir une meilleure personne.", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Tu devras valider les défis avec un certain score pour me montrer que tu as évolué", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Une fois tout les jeux fini je verrais pour t'envoyer revoir Dieu", hoppy_avatar, 'assets/images/street.png'),
    ("Personnage", "Okay Okay (Naps)", personnage_avatar, 'assets/images/street.png'),
    ("Hoppy", "Parfait de toute façon tu n'avais pas le choix ahah on rigole par ici lol xptdr", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Bon trêve de chinoiserie, dans le premier jeu tu dois attraper l'amour des gens qui tombe du ciel", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Si tu as un score de 50 je te donne accès au jeu suivant bonne chance", hoppy_avatar, 'assets/images/street.png'),
]

dialogues_loose = [
    ("Dieu", "Haha, tu es tellement nul que même un chat pourrait faire mieux que toi !", dieu_avatar_rigole, 'assets/images/sky.png'),
    ("Dieu", "Je te donnerais bien une autre chance, mais vraiment... Tu ne mérites même pas cela.", dieu_avatar_rigole, 'assets/images/sky.png'),
    ("Personnage", "C'est bon, j'ai compris !", personnage_avatar, 'assets/images/street.png'),
]

dialogues_win = [
    ("Hoppy", "Bravo ! Tu as réussi à démontrer que tu es une meilleure personne. Continue comme ça !", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Tu as prouvé que tu es prêt à évoluer. Maintenant, tu es prêt à retourner au paradis.", hoppy_avatar, 'assets/images/street.png'),
    ("Hoppy", "Bonne chance pour la suite de ton voyage. Je serai là si tu as besoin de moi.", hoppy_avatar, 'assets/images/street.png'),
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
                    if dialogue_index >= len(dialogues_intro):
                        intro_done = True
        if dialogue_index < len(dialogues_intro):
            speaker, dialogue, avatar, background_path = dialogues_intro[dialogue_index]
            local_background_image = pygame.image.load(background_path).convert_alpha()
            local_background_image = pygame.transform.scale(local_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
            screen.blit(local_background_image, (0, 0))
            draw_dialogue_box()
            draw_text(f"{speaker}: {dialogue}", (220, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 60), avatar)
        else:
            screen.blit(background_image, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

def game_over_scene(screen, font):
    global dialogue_index
    dialogue_index = 0
    while dialogue_index < len(dialogues_loose):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dialogue_index += 1
                    if dialogue_index >= len(dialogues_loose):
                        return "retry"
                elif event.key == pygame.K_ESCAPE:
                    return "quit"
        speaker, dialogue, avatar, background_path = dialogues_loose[dialogue_index]
        local_background_image = pygame.image.load(background_path).convert_alpha()
        local_background_image = pygame.transform.scale(local_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        screen.blit(local_background_image, (0, 0))
        draw_dialogue_box()
        draw_text(f"{speaker}: {dialogue}", (220, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 60), avatar)
        pygame.display.flip()
        pygame.time.Clock().tick(60)

def run_clicker_game(screen, font):
    click_goal = 30
    time_limit = 10
    clicks = 0
    start_time = pygame.time.get_ticks()
    
    click_image = pygame.image.load('assets/images/grooppy.png').convert_alpha()
    image_rect = click_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    def shake_image():
        offset = random.randint(-20, 20), random.randint(-20, 20)
        new_position = image_rect.move(offset)
        screen.blit(click_image, new_position)
        pygame.display.update()
        pygame.time.delay(50)
        screen.blit(click_image, image_rect)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and image_rect.collidepoint(event.pos):
                clicks += 1
                shake_image()
                
        current_time = pygame.time.get_ticks()
        time_elapsed = (current_time - start_time) / 1000
        time_left = max(0, time_limit - time_elapsed)
        
        if time_left == 0 or clicks >= click_goal:
            running = False
        
        screen.fill((0, 0, 0))
        screen.blit(click_image, image_rect)
        info_text = font.render(f"Clics restants: {click_goal - clicks} | Temps restant: {int(time_left)}s", True, (255, 255, 255))
        screen.blit(info_text, (10, 10))
        
        pygame.display.flip()
    
    return clicks >= click_goal

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
        if score < 50:
            action = game_over_scene(screen, font)
            if action == 'retry':
                continue
            elif action == 'quit':
                break
            score = 0
    clicker_success = run_clicker_game(screen, font)
    if clicker_success:
        print("Bravo")
    else:
        print("Dommage")

    ##appelle d'un nouveau ici jeu ici
    pygame.quit()
    sys.exit()
    pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()