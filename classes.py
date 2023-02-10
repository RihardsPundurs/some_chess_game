import pygame
from random import randint
from sys import exit


class Sector(pygame.sprite.Sprite):

    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        sector_surf1 = pygame.image.load("resources/sector1.png").convert()
        sector_surf1 = pygame.transform.scale(sector_surf1, (90, 90))
        sector_surf2 = pygame.image.load("resources/sector2.png").convert()
        sector_surf2 = pygame.transform.scale(sector_surf2, (90, 90))
        if (cords[0] % 2 == 1
                and cords[1] % 2 == 1) or (cords[0] % 2 == 0
                                           and cords[1] % 2 == 0):
            self.image = sector_surf1
        else:
            self.image = sector_surf2
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 235,
                                                  cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            print("hit GREEN")
            print(self.cords)
            return self.cords


class Pawn(pygame.sprite.Sprite):

    def __init__(self, cords, team="Blue"):
        super().__init__()
        self.cords = cords
        pawn_surf_blue = pygame.image.load(
            "resources/Finished pices/Pawn1.png").convert_alpha()
        pawn_surf_blue = pygame.transform.scale(pawn_surf_blue, (90, 90))
        pawn_surf_black = pygame.image.load(
            "resources/Finished pices/Pawn2.png").convert_alpha()
        pawn_surf_black = pygame.transform.scale(pawn_surf_black, (90, 90))
        self.team = team
        if team == "Black":
            self.image = pawn_surf_black
        else:
            self.image = pawn_surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 235,
                                                  cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            print("hit RED")
            return True

    def move(self, cords):
        print(cords)
        self.rect.x = cords[0] * 90 + 145
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        print("Done")


# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         player_surface1 = pygame.image.load("graphics/200px-ObserverSpy.png").convert_alpha()
#         player_surface1 = pygame.transform.scale(player_surface1,(85,155))
#         player_surface2 = pygame.image.load("graphics/200px-ObserverSpy.png").convert_alpha()
#         player_surface2 = pygame.transform.scale(player_surface2,(95,145))
#         self.player_jump_surface = pygame.image.load("graphics/200px-ObserverSpy.png").convert_alpha()
#         self.player_jump_surface = pygame.transform.scale(self.player_jump_surface,(110,120))
#         self.player_surface_list = [player_surface1,player_surface2]
#         self.player_index = 0

#         self.image = self.player_surface_list[self.player_index]
#         self.rect = self.image.get_rect(midbottom = (80,299))
#         self.gravity = 0

#     def player_input(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
#             self.gravity = -6

#     def apply_gravity(self):
#         self.gravity += 0.1
#         self.rect.y += self.gravity
#         if self.rect.bottom >= 300:
#             self.rect.bottom = 300

#     def animation_state(self):
#         if self.rect.bottom < 300:
#             self.image = self.player_jump_surface
#         else:
#             self.player_index += 0.02
#             if self.player_index >= len(self.player_surface_list):self.player_index = 0
#             self.image = self.player_surface_list[int(self.player_index)]

#     def update(self):
#         self.player_input()
#         self.apply_gravity()
#         self.animation_state()
