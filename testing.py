import pygame
import sys

# Init
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    # Clear screen
    screen.fill((0, 0, 0))

    
    pygame.draw.circle(screen, "magenta", (250,250), 30,10)
    pygame.draw.circle(screen, "red", (350,350), 50,20)

    

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
