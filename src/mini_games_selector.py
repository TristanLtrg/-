# import pygame
# import sys

# pygame.init()

# WINDOW_WIDTH = 1920
# WINDOW_HEIGHT = 1080
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BROWN = (165, 42, 42)
# DIALOGUE_BOX_COLOR = WHITE
# DIALOGUE_BOX_HEIGHT = 200
# DIALOGUE_TEXT_COLOR = BLACK
# AVATAR_SIZE = (150, 150)
# BORDER_THICKNESS = 5
# GRAY = (128, 128, 128)

# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Mini Games Selector")

# personnage_avatar = pygame.image.load('assets/images/player.png').convert_alpha()
# personnage_avatar = pygame.transform.scale(personnage_avatar, AVATAR_SIZE)
# dieu_avatar = pygame.image.load('assets/images/god.png').convert_alpha()
# dieu_avatar = pygame.transform.scale(dieu_avatar, AVATAR_SIZE)
# hoppy_avatar = pygame.image.load('assets/images/groppy.png').convert_alpha()
# hoppy_avatar = pygame.transform.scale(hoppy_avatar, AVATAR_SIZE)

# new_dialogues = [
#     ("Hoppy", "Bienvenue dans la rue ! Prêt à jouer à quelques mini-jeux ?", hoppy_avatar),
#     ("Personnage", "Oui, je suis prêt !", personnage_avatar),
#     ("Hoppy", "Super ! Choisissez l'un des mini-jeux ci-dessous pour commencer :", hoppy_avatar),
# ]

# button_images = [
#     pygame.image.load('assets/images/boutonss.jpg').convert_alpha(),
#     pygame.image.load('assets/images/boutonss.jpg').convert_alpha(),
#     pygame.image.load('assets/images/boutonss.jpg').convert_alpha(),
#     pygame.image.load('assets/images/boutonss.jpg').convert_alpha()
# ]

# font = pygame.font.SysFont('Arial', 22)

# def draw_text(text, position, avatar):
#     if avatar:
#         screen.blit(avatar, (60, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 35))
#     text_surface = font.render(text, True, DIALOGUE_TEXT_COLOR)
#     screen.blit(text_surface, position)

# def draw_dialogue_box():
#     pygame.draw.rect(screen, BROWN, pygame.Rect(0, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT - BORDER_THICKNESS,
#                                                  WINDOW_WIDTH, DIALOGUE_BOX_HEIGHT + (2 * BORDER_THICKNESS)))
#     pygame.draw.rect(screen, DIALOGUE_BOX_COLOR, pygame.Rect(0, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT,
#                                                              WINDOW_WIDTH, DIALOGUE_BOX_HEIGHT))

# def mini_games_selector():
#     global dialogue_index

#     new_background_image = pygame.image.load('assets/images/street.png').convert_alpha()
#     new_background_image = pygame.transform.scale(new_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

#     dialogue_index = 0
#     intro_done = False
#     while not intro_done:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     dialogue_index += 1
#                     if dialogue_index >= len(new_dialogues):
#                         intro_done = True
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if dialogue_index >= len(new_dialogues):
#                     # Si tous les dialogues sont terminés, vérifiez si un bouton a été cliqué
#                     mouse_pos = pygame.mouse.get_pos()
#                     for i, button_rect in enumerate(button_rects):
#                         if button_rect.collidepoint(mouse_pos):
#                             # Faire quelque chose lorsque le bouton est cliqué
#                             print(f"Bouton {i+1} cliqué")

#         screen.fill(BLACK)
#         screen.blit(new_background_image, (0, 0))
#         draw_dialogue_box()

#         if dialogue_index < len(new_dialogues):
#             speaker, dialogue, avatar = new_dialogues[dialogue_index]
#             draw_text(f"{speaker}: {dialogue}", (220, WINDOW_HEIGHT - DIALOGUE_BOX_HEIGHT + 60), avatar)

#         # Dessiner les boutons
#         button_rects = []
#         button_height = 50
#         for i, button_image in enumerate(button_images):
#             # Positionner les boutons à des endroits différents sur l'écran
#             button_rect = screen.blit(button_image, (100, 50 * i + 250))  # Changer les coordonnées x et y pour chaque bouton
#             button_rects.append(button_rect)

#         pygame.display.flip()
#         pygame.time.Clock().tick(60)

# if __name__ == "__main__":
#     mini_games_selector()
#     pygame.quit()
