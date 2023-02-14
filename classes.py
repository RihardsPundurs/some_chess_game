import pygame
from random import randint
from sys import exit


class Sector(pygame.sprite.Sprite):

    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        sector_surf1 = pygame.image.load("resources/ui/Black_tile.png").convert()
        sector_surf1 = pygame.transform.scale(sector_surf1, (90, 90))
        sector_surf2 = pygame.image.load("resources/ui/white_tile.png").convert()
        sector_surf2 = pygame.transform.scale(sector_surf2, (90, 90))
        if (cords[0] % 2 == 1
                and cords[1] % 2 == 1) or (cords[0] % 2 == 0
                                           and cords[1] % 2 == 0):
            self.image = sector_surf1
        else:
            self.image = sector_surf2
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280,
                                                  cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit GREEN")
            # print(self.cords)
            return self.cords

class Pawn(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], []]
        self.cords = cords
        self.team = team
        self.type = "Pawn"
        surf_black = pygame.image.load("resources/Finished pices/Pawn2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Pawn1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        if self.team == "Black":
            if self.cords[1] > 4:
                self.steps[1] = [self.cords[0] + 1, self.cords[1] + 1]
                self.steps[2] = [self.cords[0] - 1, self.cords[1] + 1]
            self.steps[0] = [self.cords[0], self.cords[1] + 1]
        else:
            if self.cords[1] < 5:
                self.steps[1] = [self.cords[0] + 1, self.cords[1] - 1]
                self.steps[2] = [self.cords[0] - 1, self.cords[1] - 1]
            self.steps[0] = [self.cords[0], self.cords[1] - 1]
        for i in friend_cords:
            if i[0] in self.steps:
                return friend_cords, [self.tag, self.type], False
            else:
                if [self.tag, self.type] in i:
                    return friend_cords, [self.tag, self.type], True
                    break

class Elephant(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], [], []]
        self.cords = cords
        self.team = team
        self.type = "Elephant"
        surf_black = pygame.image.load("resources/Finished pices/Elephant2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Elephant1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        self.steps[0] = [self.cords[0] - 2, self.cords[1] - 2]
        self.steps[1] = [self.cords[0] - 2, self.cords[1] + 2]
        self.steps[2] = [self.cords[0] + 2, self.cords[1] - 2]
        self.steps[3] = [self.cords[0] + 2, self.cords[1] + 2]

class Flamingo(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], [], [], [], [], [], []]
        self.cords = cords
        self.team = team
        self.type = "Flamingo"
        surf_black = pygame.image.load("resources/Finished pices/Flamingo2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Flamingo1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        self.steps[0] = [self.cords[0] + 6, self.cords[1] - 1]
        self.steps[1] = [self.cords[0] + 6, self.cords[1] + 1]
        self.steps[2] = [self.cords[0] - 6, self.cords[1] - 1]
        self.steps[3] = [self.cords[0] - 6, self.cords[1] + 1]
        self.steps[4] = [self.cords[0] + 1, self.cords[1] + 6]
        self.steps[5] = [self.cords[0] - 1, self.cords[1] + 6]
        self.steps[6] = [self.cords[0] + 1, self.cords[1] - 6]
        self.steps[7] = [self.cords[0] - 1, self.cords[1] - 6]

class Friend(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = []
        self.cords = cords
        self.team = team
        self.type = "Friend"
        surf_black = pygame.image.load("resources/Finished pices/Friend2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Friend1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

class GoldGeneral(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[],[],[],[],[],[]]
        self.cords = cords
        self.team = team
        self.type = "GoldGeneral"
        surf_black = pygame.image.load("resources/Finished pices/Gold_General2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Gold_General1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        if self.team == "Black":
            self.steps[0] = [self.cords[0] + 1, self.cords[1] + 1]
            self.steps[1] = [self.cords[0] - 1, self.cords[1] + 1]
            self.steps[2] = [self.cords[0], self.cords[1] + 1]
            self.steps[3] = [self.cords[0] + 1, self.cords[1]]
            self.steps[4] = [self.cords[0] - 1, self.cords[1]]
            self.steps[5] = [self.cords[0], self.cords[1] - 1]
        else:
            self.steps[0] = [self.cords[0] + 1, self.cords[1] - 1]
            self.steps[1] = [self.cords[0] - 1, self.cords[1] - 1]
            self.steps[2] = [self.cords[0], self.cords[1] - 1]
            self.steps[3] = [self.cords[0] + 1, self.cords[1]]
            self.steps[4] = [self.cords[0] - 1, self.cords[1]]
            self.steps[5] = [self.cords[0], self.cords[1] + 1]

class ZagZag(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.cords = cords
        self.team = team
        self.type = "ZagZag"
        surf_black = pygame.image.load("resources/Finished pices/Zag_Zag2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Zag_Zag1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        self.steps[0] = [self.cords[0], self.cords[1] + 1]
        self.steps[1] = [self.cords[0], self.cords[1] + 2]
        self.steps[2] = [self.cords[0], self.cords[1] + 3]
        self.steps[3] = [self.cords[0], self.cords[1] + 4]
        self.steps[4] = [self.cords[0], self.cords[1] + 5]
        self.steps[5] = [self.cords[0], self.cords[1] + 6]
        self.steps[6] = [self.cords[0], self.cords[1] + 7]
        self.steps[7] = [self.cords[0], self.cords[1] - 1]
        self.steps[8] = [self.cords[0], self.cords[1] - 2]
        self.steps[9] = [self.cords[0], self.cords[1] - 3]
        self.steps[10] = [self.cords[0], self.cords[1] - 4]
        self.steps[11] = [self.cords[0], self.cords[1] - 5]
        self.steps[12] = [self.cords[0], self.cords[1] - 6]
        self.steps[13] = [self.cords[0], self.cords[1] - 7]
        self.steps[14] = [self.cords[0] - 1, self.cords[1] + 1]
        self.steps[15] = [self.cords[0] - 2, self.cords[1] + 2]
        self.steps[16] = [self.cords[0] - 3, self.cords[1] + 3]
        self.steps[17] = [self.cords[0] - 4, self.cords[1] + 4]
        self.steps[18] = [self.cords[0] - 5, self.cords[1] + 5]
        self.steps[19] = [self.cords[0] - 6, self.cords[1] + 6]
        self.steps[20] = [self.cords[0] - 7, self.cords[1] + 7]
        self.steps[21] = [self.cords[0] + 1, self.cords[1] - 1]
        self.steps[22] = [self.cords[0] + 2, self.cords[1] - 2]
        self.steps[23] = [self.cords[0] + 3, self.cords[1] - 3]
        self.steps[24] = [self.cords[0] + 4, self.cords[1] - 4]
        self.steps[25] = [self.cords[0] + 5, self.cords[1] - 5]
        self.steps[26] = [self.cords[0] + 6, self.cords[1] - 6]
        self.steps[27] = [self.cords[0] + 7, self.cords[1] - 7]

class ZagZig(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.cords = cords
        self.team = team
        self.type = "ZagZig"
        surf_black = pygame.image.load("resources/Finished pices/Zag_Zig2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Zag_Zig1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        self.steps[0] = [self.cords[0], self.cords[1] + 1]
        self.steps[1] = [self.cords[0], self.cords[1] + 2]
        self.steps[2] = [self.cords[0], self.cords[1] + 3]
        self.steps[3] = [self.cords[0], self.cords[1] + 4]
        self.steps[4] = [self.cords[0], self.cords[1] + 5]
        self.steps[5] = [self.cords[0], self.cords[1] + 6]
        self.steps[6] = [self.cords[0], self.cords[1] + 7]
        self.steps[7] = [self.cords[0], self.cords[1] - 1]
        self.steps[8] = [self.cords[0], self.cords[1] - 2]
        self.steps[9] = [self.cords[0], self.cords[1] - 3]
        self.steps[10] = [self.cords[0], self.cords[1] - 4]
        self.steps[11] = [self.cords[0], self.cords[1] - 5]
        self.steps[12] = [self.cords[0], self.cords[1] - 6]
        self.steps[13] = [self.cords[0], self.cords[1] - 7]
        self.steps[14] = [self.cords[0] + 1, self.cords[1] + 1]
        self.steps[15] = [self.cords[0] + 2, self.cords[1] + 2]
        self.steps[16] = [self.cords[0] + 3, self.cords[1] + 3]
        self.steps[17] = [self.cords[0] + 4, self.cords[1] + 4]
        self.steps[18] = [self.cords[0] + 5, self.cords[1] + 5]
        self.steps[19] = [self.cords[0] + 6, self.cords[1] + 6]
        self.steps[20] = [self.cords[0] + 7, self.cords[1] + 7]
        self.steps[21] = [self.cords[0] - 1, self.cords[1] - 1]
        self.steps[22] = [self.cords[0] - 2, self.cords[1] - 2]
        self.steps[23] = [self.cords[0] - 3, self.cords[1] - 3]
        self.steps[24] = [self.cords[0] - 4, self.cords[1] - 4]
        self.steps[25] = [self.cords[0] - 5, self.cords[1] - 5]
        self.steps[26] = [self.cords[0] - 6, self.cords[1] - 6]
        self.steps[27] = [self.cords[0] - 7, self.cords[1] - 7]

class ZigZag(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.cords = cords
        self.team = team
        self.type = "ZigZag"
        surf_black = pygame.image.load("resources/Finished pices/Zig_Zag2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Zig_Zag1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        self.steps[0] = [self.cords[0] + 1, self.cords[1]]
        self.steps[1] = [self.cords[0] + 2, self.cords[1]]
        self.steps[2] = [self.cords[0] + 3, self.cords[1]]
        self.steps[3] = [self.cords[0] + 4, self.cords[1]]
        self.steps[4] = [self.cords[0] + 5, self.cords[1]]
        self.steps[5] = [self.cords[0] + 6, self.cords[1]]
        self.steps[6] = [self.cords[0] + 7, self.cords[1]]
        self.steps[7] = [self.cords[0] - 1, self.cords[1]]
        self.steps[8] = [self.cords[0] - 2, self.cords[1]]
        self.steps[9] = [self.cords[0] - 3, self.cords[1]]
        self.steps[10] = [self.cords[0] - 4, self.cords[1]]
        self.steps[11] = [self.cords[0] - 5, self.cords[1]]
        self.steps[12] = [self.cords[0] - 6, self.cords[1]]
        self.steps[13] = [self.cords[0] - 7, self.cords[1]]
        self.steps[14] = [self.cords[0] - 1, self.cords[1] + 1]
        self.steps[15] = [self.cords[0] - 2, self.cords[1] + 2]
        self.steps[16] = [self.cords[0] - 3, self.cords[1] + 3]
        self.steps[17] = [self.cords[0] - 4, self.cords[1] + 4]
        self.steps[18] = [self.cords[0] - 5, self.cords[1] + 5]
        self.steps[19] = [self.cords[0] - 6, self.cords[1] + 6]
        self.steps[20] = [self.cords[0] - 7, self.cords[1] + 7]
        self.steps[21] = [self.cords[0] + 1, self.cords[1] - 1]
        self.steps[22] = [self.cords[0] + 2, self.cords[1] - 2]
        self.steps[23] = [self.cords[0] + 3, self.cords[1] - 3]
        self.steps[24] = [self.cords[0] + 4, self.cords[1] - 4]
        self.steps[25] = [self.cords[0] + 5, self.cords[1] - 5]
        self.steps[26] = [self.cords[0] + 6, self.cords[1] - 6]
        self.steps[27] = [self.cords[0] + 7, self.cords[1] - 7]

class ZigZig(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        self.cords = cords
        self.team = team
        self.type = "ZigZig"
        surf_black = pygame.image.load("resources/Finished pices/Zig_Zig2.png").convert_alpha()
        surf_black = pygame.transform.scale(surf_black, (90, 90))
        surf_blue = pygame.image.load("resources/Finished pices/Zig_Zig1.png").convert_alpha()
        surf_blue = pygame.transform.scale(surf_blue, (90, 90))
        if self.team == "Black":
            self.image = surf_black
        else:
            self.image = surf_blue
        self.rect = self.image.get_rect(topright=(cords[0] * 90 + 280, cords[1] * 90 - 90))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            # print("hit RED")
            return True

    def move(self, cords):
        # print(cords)
        self.rect.x = cords[0] * 90 + 190
        self.rect.y = cords[1] * 90 - 90
        self.cords = cords
        # print("Done")

    def take(self): #, cords
        print("zahamn")

    def destroy(self):
        self.kill()

    def update(self, friend_cords):
        self.steps[0] = [self.cords[0] + 1, self.cords[1]]
        self.steps[1] = [self.cords[0] + 2, self.cords[1]]
        self.steps[2] = [self.cords[0] + 3, self.cords[1]]
        self.steps[3] = [self.cords[0] + 4, self.cords[1]]
        self.steps[4] = [self.cords[0] + 5, self.cords[1]]
        self.steps[5] = [self.cords[0] + 6, self.cords[1]]
        self.steps[6] = [self.cords[0] + 7, self.cords[1]]
        self.steps[7] = [self.cords[0] - 1, self.cords[1]]
        self.steps[8] = [self.cords[0] - 2, self.cords[1]]
        self.steps[9] = [self.cords[0] - 3, self.cords[1]]
        self.steps[10] = [self.cords[0] - 4, self.cords[1]]
        self.steps[11] = [self.cords[0] - 5, self.cords[1]]
        self.steps[12] = [self.cords[0] - 6, self.cords[1]]
        self.steps[13] = [self.cords[0] - 7, self.cords[1]]
        self.steps[14] = [self.cords[0] + 1, self.cords[1] + 1]
        self.steps[15] = [self.cords[0] + 2, self.cords[1] + 2]
        self.steps[16] = [self.cords[0] + 3, self.cords[1] + 3]
        self.steps[17] = [self.cords[0] + 4, self.cords[1] + 4]
        self.steps[18] = [self.cords[0] + 5, self.cords[1] + 5]
        self.steps[19] = [self.cords[0] + 6, self.cords[1] + 6]
        self.steps[20] = [self.cords[0] + 7, self.cords[1] + 7]
        self.steps[21] = [self.cords[0] - 1, self.cords[1] - 1]
        self.steps[22] = [self.cords[0] - 2, self.cords[1] - 2]
        self.steps[23] = [self.cords[0] - 3, self.cords[1] - 3]
        self.steps[24] = [self.cords[0] - 4, self.cords[1] - 4]
        self.steps[25] = [self.cords[0] - 5, self.cords[1] - 5]
        self.steps[26] = [self.cords[0] - 6, self.cords[1] - 6]
        self.steps[27] = [self.cords[0] - 7, self.cords[1] - 7]

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
