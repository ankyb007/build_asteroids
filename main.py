import sys
import pygame
from asteroidfield import *
from asteroid import *
from player import *
from constants import *
from shots import *
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    p1=pygame.time.Clock()
    dt=0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    splittable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    p2=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable, drawable, splittable)

    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable, drawable) 



    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroid_group:
            if p2.check_collision(asteroid):
                print("Game Over")
                sys.exit()

            for shot in shots_group:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        #for asteroid in asteroid_group:
            #collided_bullets = pygame.sprite.spritecollide(asteroid, shots_group, True)
            #if collided_bullets:
                #asteroid.kill()




        for thing in drawable:
            thing.draw(screen)
        # p2.update(dt)
        # p2.draw(screen)
        pygame.display.flip()
        dt=(p1.tick(60))/1000
   


if __name__ == "__main__":
    main()
