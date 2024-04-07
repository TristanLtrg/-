import pygame
import random
import sys

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

def run_clicker_game(screen, font):
    click_goal = 30
    time_limit = 10
    clicks = 0
    start_time = pygame.time.get_ticks()
    
    background_image = pygame.image.load('assets/images/tea.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    click_image = pygame.image.load('assets/images/grooppy.png').convert_alpha()
    image_rect = click_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    click_sound = pygame.mixer.Sound('assets/musics/purr.mp3')

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
                click_sound.play()
                shake_image()
                
        current_time = pygame.time.get_ticks()
        time_elapsed = (current_time - start_time) / 1000
        time_left = max(0, time_limit - time_elapsed)
        
        if time_left == 0 or clicks >= click_goal:
            running = False
        
        screen.blit(background_image, (0, 0))
        screen.blit(click_image, image_rect)
        info_text = font.render(f"Clics restants: {click_goal - clicks} | Temps restant: {int(time_left)}s", True, (255, 255, 255))
        screen.blit(info_text, (10, 10))
        
        pygame.display.flip()
    
    return clicks >= click_goal

def run_cleaning_game(screen, font):
    start_time = pygame.time.get_ticks()
    time_limit = 60000
    
    background_image = pygame.image.load('assets/images/place.png').convert_alpha()
    background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    poubelle_image = pygame.image.load('assets/images/poubelle.png').convert_alpha()
    poubelle_rect = poubelle_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    dechets = [pygame.image.load(f'assets/images/dechet{i % 3 + 1}.png').convert_alpha() for i in range(20)]
    dechet_rects = [dechet.get_rect(topleft=(random.randint(0, screen.get_width() - 100), random.randint(0, screen.get_height() - 100))) for dechet in dechets]
    
    dragging = None
    offset_x = offset_y = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(dechet_rects):
                    if rect.collidepoint(event.pos):
                        dragging = i
                        mouse_x, mouse_y = event.pos
                        offset_x = rect.x - mouse_x
                        offset_y = rect.y - mouse_y
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging is not None and poubelle_rect.collidepoint(event.pos):
                    dechets.pop(dragging)
                    dechet_rects.pop(dragging)
                dragging = None
            elif event.type == pygame.MOUSEMOTION and dragging is not None:
                mouse_x, mouse_y = event.pos
                dechet_rects[dragging].x = mouse_x + offset_x
                dechet_rects[dragging].y = mouse_y + offset_y
        
        current_time = pygame.time.get_ticks()
        if current_time - start_time > time_limit or not dechets:
            running = False
        
        screen.blit(background_image, (0, 0))
        for dechet, rect in zip(dechets, dechet_rects):
            screen.blit(dechet, rect)
        screen.blit(poubelle_image, poubelle_rect)
        
        time_left = max(0, (time_limit - (current_time - start_time)) // 1000)
        time_text = font.render(f"Temps restant: {time_left}s", True, (0, 0, 0))
        screen.blit(time_text, (10, 10))
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    
    return not dechets

def run_door_game(screen, font):
    porte_fermee = pygame.image.load('assets/images/dechet1.png').convert_alpha()
    porte_ouverte_correcte = pygame.image.load('assets/images/dechet2.png').convert_alpha()
    porte_ouverte_incorrecte = pygame.image.load('assets/images/dechet3.png').convert_alpha()
    door_width, door_height = porte_fermee.get_size()
    doors = [
        porte_fermee.get_rect(topleft=(100, screen.get_height() // 2 - door_height // 2)),
        porte_fermee.get_rect(topleft=(650, screen.get_height() // 2 - door_height // 2)),
        porte_fermee.get_rect(topleft=(1200, screen.get_height() // 2 - door_height // 2))
    ]
    correct_door = random.randint(0, 2)
    door_states = ['closed', 'closed', 'closed']
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(doors):
                    if rect.collidepoint(event.pos):
                        if i == correct_door:
                            door_states[i] = 'correct'
                        else:
                            door_states[i] = 'incorrect'
                        running = False
                        
        screen.fill((255, 255, 255))
        
        for i, rect in enumerate(doors):
            if door_states[i] == 'closed':
                screen.blit(porte_fermee, rect)
            elif door_states[i] == 'correct':
                screen.blit(porte_ouverte_correcte, rect)
            else:
                screen.blit(porte_ouverte_incorrecte, rect)
        
        pygame.display.flip()
    
    if 'correct' in door_states:
        return True
    return False