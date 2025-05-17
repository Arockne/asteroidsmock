from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from constants import ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
import pygame

def main():
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  while True:
    #check player inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    #update game world
    screen.fill("black")
    #draw game on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000
  
if __name__ == "__main__":
    main()