import pygame
from random import randint
from sys import exit
from classes import *

pygame.init()
screen = pygame.display.set_mode((1280, 720), )  #pygame.FULLSCREEN
pygame.display.set_caption("Placeholder title")
clock = pygame.time.Clock()
game_active = False
lift = [False, None]
set_cords = [None, None]
info = []

test_font = pygame.font.Font(None, 50)

# player = pygame.sprite.GroupSingle()
# player.add(Player())

text_surf = test_font.render("TEST", False, "White")
bg_surf = pygame.image.load("resources/ui/bg2.png").convert()
bg_surf = pygame.transform.scale(bg_surf, (1280, 720))
bg_rect = bg_surf.get_rect(center=(640, 360))

board = pygame.sprite.Group()
for i1 in range(1, 10):
  for i2 in range(1, 10):
    board.add(Sector([i1, i2]))

pieces = pygame.sprite.Group()
pieces.add(Pawn([1, 1], len(info), "Black"))
info.append(["Pawn", "Black", [1, 1]])
pieces.add(Pawn([2, 1], len(info), "Black"))
info.append(["Pawn", "Black", [2, 1]])

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

    # if game_active:
    #     if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #         game_active = True
    #         start_time = pygame.time.get_ticks()

    elif event.type == pygame.MOUSEBUTTONDOWN:
      if not lift[0]:
        for i in pieces:
          lift[0] = i.check_click(event.pos)
          if lift[0]:
            lift[1] = i
            break
      else:
        for i1 in board:
          set_cords = i1.check_click(event.pos)
          if set_cords != None:
            piece_cords = []
            for i2 in info:
              piece_cords.append(i2[2])
            if set_cords not in piece_cords:
              lift[1].move(set_cords)
              info[lift[1].tag][2] = set_cords
              set_cords = None
              lift = [False, None]
              break
            # if set_cords in piece_cords:
            #   lift[1].move(set_cords)
            #   info[lift[1].tag][2] = set_cords
            #   set_cords = None
            #   lift = [False, None]
            #   break




        # for i in board:
        #     set_cords = i.check_click(event.pos)
        #     if s.check_click(event.pos):
        #         s.move(set_cords)

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RETURN]:
    game_active = True

  if game_active:
    screen.blit(bg_surf, bg_rect)
    board.draw(screen)
    board.update()
    pieces.draw(screen)
    pieces.update()

  else:
    screen.blit(bg_surf, bg_rect)
    screen.blit(text_surf, (640, 360))
  pygame.display.update()
  clock.tick(60)
