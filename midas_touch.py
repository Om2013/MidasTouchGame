import pygame
pygame.init()
pygame.mixer.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)

# Sound
pick_up_sound = pygame.mixer.Sound(r"C:\Users\omrad\OneDrive\Desktop\OtherUser - CodingProjects\Midas Touch Game\pick_up_sound.wav")

# Screen
WINDOW_SIZE = 600
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Midas Touch Game")

# FPS
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 70)

# Settings
SIZE = 50
SPEED = 5
TIME_LIMIT = 10  # seconds

# Reset function
def reset_game():
    x = 275
    y = 275
    midas_dx = 0
    midas_dy = 0

    touched_rect1 = False
    touched_rect2 = False
    touched_rect3 = False
    touched_rect4 = False

    start_time = pygame.time.get_ticks()
    won = False
    lost = False

    return x, y, midas_dx, midas_dy, touched_rect1, touched_rect2, touched_rect3, touched_rect4, start_time, won, lost

x, y, midas_dx, midas_dy, touched_rect1, touched_rect2, touched_rect3, touched_rect4, start_time, won, lost = reset_game()

midas = pygame.Rect(x, y, SIZE, SIZE)

# Rectangles
rect1 = pygame.Rect(20, 20, 70, 70)
rect2 = pygame.Rect(510, 20, 70, 70)
rect3 = pygame.Rect(20, 510, 70, 70)
rect4 = pygame.Rect(510, 510, 70, 70)

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                midas_dx = -SPEED
                midas_dy = 0
            elif event.key == pygame.K_RIGHT:
                midas_dx = SPEED
                midas_dy = 0
            elif event.key == pygame.K_UP:
                midas_dx = 0
                midas_dy = -SPEED
            elif event.key == pygame.K_DOWN:
                midas_dx = 0
                midas_dy = SPEED

            # Restart
            elif event.key == pygame.K_r:
                x, y, midas_dx, midas_dy, touched_rect1, touched_rect2, touched_rect3, touched_rect4, start_time, won, lost = reset_game()

    # Timer (countdown)
    if not won and not lost:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) // 1000
        time_left = TIME_LIMIT - elapsed_time

        if time_left <= 0:
            lost = True

    # Movement
    if not won and not lost:
        x += midas_dx
        y += midas_dy

        x = max(0, min(x, WINDOW_SIZE - SIZE))
        y = max(0, min(y, WINDOW_SIZE - SIZE))

    midas.x = x
    midas.y = y

    # Collisions
    if not won and not lost:

        if midas.colliderect(rect1) and not touched_rect1:
            touched_rect1 = True
            pick_up_sound.play()

        if midas.colliderect(rect2) and not touched_rect2:
            touched_rect2 = True
            pick_up_sound.play()

        if midas.colliderect(rect3) and not touched_rect3:
            touched_rect3 = True
            pick_up_sound.play()

        if midas.colliderect(rect4) and not touched_rect4:
            touched_rect4 = True
            pick_up_sound.play()

    # Win condition
    if touched_rect1 and touched_rect2 and touched_rect3 and touched_rect4:
        won = True

    # Draw
    screen.fill(WHITE)

    pygame.draw.rect(screen, ORANGE, midas)

    pygame.draw.rect(screen, GOLD if touched_rect1 else RED, rect1)
    pygame.draw.rect(screen, GOLD if touched_rect2 else BLUE, rect2)
    pygame.draw.rect(screen, GOLD if touched_rect3 else YELLOW, rect3)
    pygame.draw.rect(screen, GOLD if touched_rect4 else GREEN, rect4)

    # Centered timer
    if not won and not lost:
        color = RED if time_left <= 2 else BLACK
        timer_text = font.render(f"Time Left: {time_left}", True, color)
        text_rect = timer_text.get_rect(center=(WINDOW_SIZE // 2, 30))
        screen.blit(timer_text, text_rect)

    # Win screen
    if won:
        win_text = big_font.render("YOU WIN!", True, BLACK)
        screen.blit(win_text, (180, 250))

        restart_text = font.render("Press R to Restart", True, BLACK)
        screen.blit(restart_text, (190, 320))

    # Lose screen
    if lost:
        lose_text = big_font.render("YOU LOSE!", True, BLACK)
        screen.blit(lose_text, (180, 250))

        restart_text = font.render("Press R to Restart", True, BLACK)
        screen.blit(restart_text, (190, 320))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
