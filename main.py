import pygame
from random import randint
from sys import exit
from classes import *

pygame.init()
screen = pygame.display.set_mode((1280, 720), )  #pygame.FULLSCREEN
pygame.display.set_caption("Placeholder title")
clock = pygame.time.Clock()
game_active = False

test_font = pygame.font.Font(None, 50)

# player = pygame.sprite.GroupSingle()
# player.add(Player())

text_surf = test_font.render("TEST", False, "White")
grid_surf = pygame.image.load("resources/pixil-frame-0.png").convert()
grid_surf = pygame.transform.scale(grid_surf, (720, 720))
grid_rect = grid_surf.get_rect(center=(640, 360))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

    # if game_active:
    #     if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #         game_active = True
    #         start_time = pygame.time.get_ticks()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RETURN]:
    game_active = True

  if game_active:
    screen.blit(grid_surf, grid_rect)
    # player.draw(screen)
    # player.update()

  else:
    screen.blit(text_surf, (640, 360))
  pygame.display.update()
  clock.tick(60)
