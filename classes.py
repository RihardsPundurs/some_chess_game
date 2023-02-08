class Sector(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        sector_surf1 = pygame.image.load("resources/sector1.png").convert()
        sector_surf1 = pygame.transform.scale(90, 90)
        sector_surf2 = pygame.image.load("resources/sector2.png").convert()
        sector_surf2 = pygame.transform.scale(90, 90)
        self.sector_surf_list = [sector_surf1, sector_surf2]

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
