from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from constants import ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
import pygame, sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  #system info
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  #groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  #containers
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  #initialized objects
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  #game loop
  while True:
    #check player inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    #update game world
    screen.fill("black")
    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.collides(player):
        print("Game over!")
        sys.exit()

    #draw game on screen
    for entity in drawable:
      entity.draw(screen)
    
    pygame.display.flip()

    #limit to 60 FPS
    dt = clock.tick(60) / 1000
  
if __name__ == "__main__":
    main()