# Import pygame
import pygame

# Initialize Pygame
pygame.init()

# Give the RGB for the colors 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GOLD = (212, 175, 55)
ORANGE = (255, 165, 0)

# Give the sound audio
pick_up_sound = pygame.mixer.Sound(r"C:\Users\omrad\OneDrive\Desktop\Midas Touch Game\pick_up_sound.wav")

# Set up the screen
display = pygame.display.set_mode((600, 600))
pygame.display.set_caption("The Midas Touch")

# FPS Settings
clock = pygame.time.Clock()
FPS = 5

# Give all the variables needed for the project
x = 275
y = 275
midas_dx = 0
midas_dy = 0
SIZE = 50

# Make the Midas rectangle 
midas = pygame.Rect(x, y, SIZE, SIZE)

# Make the 4 rectangles 
rect1 = pygame.Rect(20, 20, 70, 70)
rect2 = pygame.Rect(510, 20, 70, 70)
rect3 = pygame.Rect(20, 510, 70, 70)
rect4 = pygame.Rect(510, 510, 70, 70)

# Set the rectangles to not touched 
touched1 = False
touched2 = False
touched3 = False
touched4 = False

# Gameloop
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and midas_dx == 0:
                midas_dx = -SIZE
                midas_dy = 0
            elif event.key == pygame.K_RIGHT and midas_dx == 0:
                midas_dx = SIZE
                midas_dy = 0
            elif event.key == pygame.K_UP and midas_dy == 0:
                midas_dx = 0
                midas_dy = -SIZE
            elif event.key == pygame.K_DOWN and midas_dy == 0:
                midas_dx = 0
                midas_dy = SIZE

    x += midas_dx
    y += midas_dy
    midas = pygame.Rect(x, y, SIZE, SIZE)

    # Check the collison
    if midas.colliderect(rect1) and not touched1:
        touched1 = True
        pick_up_sound.play()
    if midas.colliderect(rect2) and not touched2:
        touched2 = True
        pick_up_sound.play()
    if midas.colliderect(rect3) and not touched3:
        touched3 = True
        pick_up_sound.play()
    if midas.colliderect(rect4) and not touched4:
        touched4 = True
        pick_up_sound.play()

    display.fill(WHITE)
    pygame.draw.rect(display, GOLD if touched1 else RED, rect1)
    pygame.draw.rect(display, GOLD if touched2 else GREEN, rect2)
    pygame.draw.rect(display, GOLD if touched3 else BLUE, rect3)
    pygame.draw.rect(display, GOLD if touched4 else YELLOW, rect4)
    pygame.draw.rect(display, ORANGE, midas)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
