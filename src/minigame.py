import pygame
import random

def run_minigame(screen, font):
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    PLAYER_SIZE = (200, 200)
    GOOD_ACTION_SIZE = 20
    GOOD_ACTION_FALL_SPEED = 0.5
    GAME_DURATION = 28
    FRAME_DURATION = 300
    score = 0
    full_body_image = pygame.image.load('assets/images/fullBody.png').convert_alpha()
    full_body_image = pygame.transform.scale(full_body_image, (2 * PLAYER_SIZE[0], PLAYER_SIZE[1]))
    heart_image = pygame.image.load('assets/images/heart.png').convert_alpha()
    heart_image = pygame.transform.scale(heart_image, (GOOD_ACTION_SIZE * 2, GOOD_ACTION_SIZE * 2))
    background_image = pygame.image.load('assets/images/street_bckg.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))
    player_pos = [screen.get_width() // 2, screen.get_height() - PLAYER_SIZE[1] - 150]
    good_actions = []
    last_frame_update_time = pygame.time.get_ticks()
    current_frame = 0
    start_time = pygame.time.get_ticks()
    running = True
    pygame.mixer.music.load('assets/musics/nya.mp3')
    pygame.mixer.music.play(-1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            player_pos[0] -= 2
        if keys[pygame.K_d]:
            player_pos[0] += 2
        player_pos[0] = max(0, min(screen.get_width() - PLAYER_SIZE[0], player_pos[0]))
        screen.blit(background_image, (0, 0))
        current_time = pygame.time.get_ticks()
        if current_time - last_frame_update_time > FRAME_DURATION:
            current_frame = (current_frame + 1) % 2
            last_frame_update_time = current_time
        frame_rect = pygame.Rect(current_frame * PLAYER_SIZE[0], 0, PLAYER_SIZE[0], PLAYER_SIZE[1])
        player_frame = full_body_image.subsurface(frame_rect)
        screen.blit(player_frame, player_pos)
        if random.randint(1, 60) == 1:
            good_actions.append([random.randint(0, screen.get_width() - GOOD_ACTION_SIZE * 2), 0])
        for action in good_actions[:]:
            action[1] += GOOD_ACTION_FALL_SPEED
            if action[1] > screen.get_height():
                good_actions.remove(action)
            else:
                screen.blit(heart_image, (action[0], action[1]))
                if player_pos[0] <= action[0] <= player_pos[0] + PLAYER_SIZE[0] and player_pos[1] <= action[1] <= player_pos[1] + PLAYER_SIZE[1]:
                    score += 1
                    good_actions.remove(action)
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        time_left = max(0, GAME_DURATION - elapsed_time)
        info_text = font.render(f"Score: {score} / 50 | Time Left: {time_left}s", True, RED)
        screen.blit(info_text, (10, 10))
        if elapsed_time >= GAME_DURATION or score >= 50:
            running = False
            pygame.mixer.music.stop()
        pygame.display.flip()
    return score