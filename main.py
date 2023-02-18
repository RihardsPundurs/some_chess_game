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
for i1 in range(1, 9):
  for i2 in range(1, 9):
    board.add(Sector([i1, i2]))

pieces = pygame.sprite.Group()
pieces.add(Elephant([1, 1], len(info), "Black"))
info.append(["Elephant", "Black", [1, 1]])
pieces.add(Flamingo([2, 1], len(info), "Black"))
info.append(["Flamingo", "Black", [2, 1]])
pieces.add(Friend([3, 1], len(info), "Black"))
info.append(["Friend", "Black", [3, 1]])
pieces.add(GoldGeneral([4, 1], len(info), "Black"))
info.append(["GoldGeneral", "Black", [4, 1]])
pieces.add(ZagZag([5, 1], len(info), "Black"))
info.append(["ZagZag", "Black", [5, 1]])
pieces.add(ZagZig([6, 1], len(info), "Black"))
info.append(["ZagZig", "Black", [6, 1]])
pieces.add(ZigZag([7, 1], len(info), "Black"))
info.append(["ZigZag", "Black", [7, 1]])
pieces.add(ZigZig([8, 1], len(info), "Black"))
info.append(["ZigZig", "Black", [8, 1]])
pieces.add(Pawn([1, 2], len(info), "Black"))
info.append(["Pawn", "Black", [1, 2]])

pieces.add(Elephant([1, 8], len(info), "Blue"))
info.append(["Elephant", "Blue", [1, 8]])
pieces.add(Flamingo([2, 8], len(info), "Blue"))
info.append(["Flamingo", "Blue", [2, 8]])
pieces.add(Friend([3, 8], len(info), "Blue"))
info.append(["Friend", "Blue", [3, 8]])
pieces.add(GoldGeneral([4, 8], len(info), "Blue"))
info.append(["GoldGeneral", "Blue", [4, 8]])
pieces.add(ZagZag([5, 8], len(info), "Blue"))
info.append(["ZagZag", "Blue", [5, 8]])
pieces.add(ZagZig([6, 8], len(info), "Blue"))
info.append(["ZagZig", "Blue", [6, 8]])
pieces.add(ZigZag([7, 8], len(info), "Blue"))
info.append(["ZigZag", "Blue", [7, 8]])
pieces.add(ZigZig([8, 8], len(info), "Blue"))
info.append(["ZigZig", "Blue", [8, 8]])
pieces.add(Pawn([1, 7], len(info), "Blue"))
info.append(["Pawn", "Blue", [1, 7]])

friend_cords = []
for i in pieces:
  if i.type == "Friend":
    friend_cords.append([i.cords])

print(friend_cords)

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
          if set_cords != None and set_cords in i.steps:
            piece_cords = []
            piece_teams = []
            for i2 in info:
              piece_cords.append(i2[2])
              piece_teams.append(i2[1])
            if set_cords not in piece_cords:
              lift[1].move(set_cords)
              info[lift[1].tag][2] = set_cords
              set_cords = None
              lift = [False, None]
              break
            if set_cords in piece_cords:
              if lift[1].team != info[piece_cords.index(set_cords)][1]:
                lift[1].move(set_cords)
                lift[1].take()
                info[lift[1].tag][2] = set_cords
                lift = [False, None]
                i3 = None
                for i4 in range(piece_cords.index(set_cords), len(info)-1):
                  for i5 in pieces:
                    if i5.tag == i4+1:
                      i5.tag = i4
                info.pop(piece_cords.index(set_cords))
                for i3 in pieces:
                  if i3.tag == piece_cords.index(set_cords):
                    i3.destroy()
                    break
                set_cords = None
                break




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
    print("00", friend_cords)
    for z in pieces:
      friend_cords = z.update(friend_cords)
    print("11", friend_cords)

  else:
    screen.blit(bg_surf, bg_rect)
    screen.blit(text_surf, (640, 360))
  pygame.display.update()
  clock.tick(60)
