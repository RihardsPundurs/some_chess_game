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

    def destroy(self ):
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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("1", friend_cords)
        return friend_cords



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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("2", friend_cords)
        return friend_cords

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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("3", friend_cords)
        return friend_cords

class Friend(pygame.sprite.Sprite):
    def __init__(self, cords, tag, team="Blue"):
        super().__init__()
        self.tag = tag
        self.steps = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
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

    def update(self, friend_cords):
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("4", friend_cords)

        i2 = []
        for x in friend_cords:
            i2 = x
            if i2[0] == self.cords:
                list_of_types = []
                i2.pop(0)
                for i3 in i2:
                    list_of_types.append(i3)
                print(list_of_types)
                if "Pawn" in list_of_types:
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
                else:
                    self.steps[1] = [None, None]
                    self.steps[2] = [None, None]
                    self.steps[0] = [None, None] 
                if "Elephant" in list_of_types:
                    self.steps[0 + 3] = [self.cords[0] - 2, self.cords[1] - 2]
                    self.steps[1 + 3] = [self.cords[0] - 2, self.cords[1] + 2]
                    self.steps[2 + 3] = [self.cords[0] + 2, self.cords[1] - 2]
                    self.steps[3 + 3] = [self.cords[0] + 2, self.cords[1] + 2]
                else:
                    self.steps[0 + 3] = [None, None]
                    self.steps[1 + 3] = [None, None]
                    self.steps[2 + 3] = [None, None]
                    self.steps[3 + 3] = [None, None]
                if "Flamingo" in list_of_types:
                    self.steps[0 + 7] = [self.cords[0] + 6, self.cords[1] - 1]
                    self.steps[1 + 7] = [self.cords[0] + 6, self.cords[1] + 1]
                    self.steps[2 + 7] = [self.cords[0] - 6, self.cords[1] - 1]
                    self.steps[3 + 7] = [self.cords[0] - 6, self.cords[1] + 1]
                    self.steps[4 + 7] = [self.cords[0] + 1, self.cords[1] + 6]
                    self.steps[5 + 7] = [self.cords[0] - 1, self.cords[1] + 6]
                    self.steps[6 + 7] = [self.cords[0] + 1, self.cords[1] - 6]
                    self.steps[7 + 7] = [self.cords[0] - 1, self.cords[1] - 6]
                else:
                    self.steps[0 + 7] = [None, None]
                    self.steps[1 + 7] = [None, None]
                    self.steps[2 + 7] = [None, None]
                    self.steps[3 + 7] = [None, None]
                    self.steps[4 + 7] = [None, None]
                    self.steps[5 + 7] = [None, None]
                    self.steps[6 + 7] = [None, None]
                    self.steps[7 + 7] = [None, None]
                # if "Friend" in list_of_types:
                #     pass
                if "GoldGeneral" in list_of_types:
                    if self.team == "Black":
                        self.steps[0 + 15] = [self.cords[0] + 1, self.cords[1] + 1]
                        self.steps[1 + 15] = [self.cords[0] - 1, self.cords[1] + 1]
                        self.steps[2 + 15] = [self.cords[0], self.cords[1] + 1]
                        self.steps[3 + 15] = [self.cords[0] + 1, self.cords[1]]
                        self.steps[4 + 15] = [self.cords[0] - 1, self.cords[1]]
                        self.steps[5 + 15] = [self.cords[0], self.cords[1] - 1]
                    else:
                        self.steps[0 + 15] = [self.cords[0] + 1, self.cords[1] - 1]
                        self.steps[1 + 15] = [self.cords[0] - 1, self.cords[1] - 1]
                        self.steps[2 + 15] = [self.cords[0], self.cords[1] - 1]
                        self.steps[3 + 15] = [self.cords[0] + 1, self.cords[1]]
                        self.steps[4 + 15] = [self.cords[0] - 1, self.cords[1]]
                        self.steps[5 + 15] = [self.cords[0], self.cords[1] + 1]
                else:
                    self.steps[0 + 15] = [None, None]
                    self.steps[1 + 15] = [None, None]
                    self.steps[2 + 15] = [None, None]
                    self.steps[3 + 15] = [None, None]
                    self.steps[4 + 15] = [None, None]
                    self.steps[5 + 15] = [None, None]
                if "ZagZag" in list_of_types:
                    self.steps[0 + 21] = [self.cords[0], self.cords[1] + 1]
                    self.steps[1 + 21] = [self.cords[0], self.cords[1] + 2]
                    self.steps[2 + 21] = [self.cords[0], self.cords[1] + 3]
                    self.steps[3 + 21] = [self.cords[0], self.cords[1] + 4]
                    self.steps[4 + 21] = [self.cords[0], self.cords[1] + 5]
                    self.steps[5 + 21] = [self.cords[0], self.cords[1] + 6]
                    self.steps[6 + 21] = [self.cords[0], self.cords[1] + 7]
                    self.steps[7 + 21] = [self.cords[0], self.cords[1] - 1]
                    self.steps[8 + 21] = [self.cords[0], self.cords[1] - 2]
                    self.steps[9 + 21] = [self.cords[0], self.cords[1] - 3]
                    self.steps[10 + 21] = [self.cords[0], self.cords[1] - 4]
                    self.steps[11 + 21] = [self.cords[0], self.cords[1] - 5]
                    self.steps[12 + 21] = [self.cords[0], self.cords[1] - 6]
                    self.steps[13 + 21] = [self.cords[0], self.cords[1] - 7]
                    self.steps[14 + 21] = [self.cords[0] - 1, self.cords[1] + 1]
                    self.steps[15 + 21] = [self.cords[0] - 2, self.cords[1] + 2]
                    self.steps[16 + 21] = [self.cords[0] - 3, self.cords[1] + 3]
                    self.steps[17 + 21] = [self.cords[0] - 4, self.cords[1] + 4]
                    self.steps[18 + 21] = [self.cords[0] - 5, self.cords[1] + 5]
                    self.steps[19 + 21] = [self.cords[0] - 6, self.cords[1] + 6]
                    self.steps[20 + 21] = [self.cords[0] - 7, self.cords[1] + 7]
                    self.steps[21 + 21] = [self.cords[0] + 1, self.cords[1] - 1]
                    self.steps[22 + 21] = [self.cords[0] + 2, self.cords[1] - 2]
                    self.steps[23 + 21] = [self.cords[0] + 3, self.cords[1] - 3]
                    self.steps[24 + 21] = [self.cords[0] + 4, self.cords[1] - 4]
                    self.steps[25 + 21] = [self.cords[0] + 5, self.cords[1] - 5]
                    self.steps[26 + 21] = [self.cords[0] + 6, self.cords[1] - 6]
                    self.steps[27 + 21] = [self.cords[0] + 7, self.cords[1] - 7]
                else:
                    self.steps[0 + 21] = [None, None]
                    self.steps[1 + 21] = [None, None]
                    self.steps[2 + 21] = [None, None]
                    self.steps[3 + 21] = [None, None]
                    self.steps[4 + 21] = [None, None]
                    self.steps[5 + 21] = [None, None]
                    self.steps[6 + 21] = [None, None]
                    self.steps[7 + 21] = [None, None]
                    self.steps[8 + 21] = [None, None]
                    self.steps[9 + 21] = [None, None]
                    self.steps[10 + 21] = [None, None]
                    self.steps[11 + 21] = [None, None]
                    self.steps[12 + 21] = [None, None]
                    self.steps[13 + 21] = [None, None]
                    self.steps[14 + 21] = [None, None]
                    self.steps[15 + 21] = [None, None]
                    self.steps[16 + 21] = [None, None]
                    self.steps[17 + 21] = [None, None]
                    self.steps[18 + 21] = [None, None]
                    self.steps[19 + 21] = [None, None]
                    self.steps[20 + 21] = [None, None]
                    self.steps[21 + 21] = [None, None]
                    self.steps[22 + 21] = [None, None]
                    self.steps[23 + 21] = [None, None]
                    self.steps[24 + 21] = [None, None]
                    self.steps[25 + 21] = [None, None]
                    self.steps[26 + 21] = [None, None]
                    self.steps[27 + 21] = [None, None]
                if "ZagZig" in list_of_types:
                    self.steps[0 + 49] = [self.cords[0], self.cords[1] + 1]
                    self.steps[1 + 49] = [self.cords[0], self.cords[1] + 2]
                    self.steps[2 + 49] = [self.cords[0], self.cords[1] + 3]
                    self.steps[3 + 49] = [self.cords[0], self.cords[1] + 4]
                    self.steps[4 + 49] = [self.cords[0], self.cords[1] + 5]
                    self.steps[5 + 49] = [self.cords[0], self.cords[1] + 6]
                    self.steps[6 + 49] = [self.cords[0], self.cords[1] + 7]
                    self.steps[7 + 49] = [self.cords[0], self.cords[1] - 1]
                    self.steps[8 + 49] = [self.cords[0], self.cords[1] - 2]
                    self.steps[9 + 49] = [self.cords[0], self.cords[1] - 3]
                    self.steps[10 + 49] = [self.cords[0], self.cords[1] - 4]
                    self.steps[11 + 49] = [self.cords[0], self.cords[1] - 5]
                    self.steps[12 + 49] = [self.cords[0], self.cords[1] - 6]
                    self.steps[13 + 49] = [self.cords[0], self.cords[1] - 7]
                    self.steps[14 + 49] = [self.cords[0] + 1, self.cords[1] + 1]
                    self.steps[15 + 49] = [self.cords[0] + 2, self.cords[1] + 2]
                    self.steps[16 + 49] = [self.cords[0] + 3, self.cords[1] + 3]
                    self.steps[17 + 49] = [self.cords[0] + 4, self.cords[1] + 4]
                    self.steps[18 + 49] = [self.cords[0] + 5, self.cords[1] + 5]
                    self.steps[19 + 49] = [self.cords[0] + 6, self.cords[1] + 6]
                    self.steps[20 + 49] = [self.cords[0] + 7, self.cords[1] + 7]
                    self.steps[21 + 49] = [self.cords[0] - 1, self.cords[1] - 1]
                    self.steps[22 + 49] = [self.cords[0] - 2, self.cords[1] - 2]
                    self.steps[23 + 49] = [self.cords[0] - 3, self.cords[1] - 3]
                    self.steps[24 + 49] = [self.cords[0] - 4, self.cords[1] - 4]
                    self.steps[25 + 49] = [self.cords[0] - 5, self.cords[1] - 5]
                    self.steps[26 + 49] = [self.cords[0] - 6, self.cords[1] - 6]
                    self.steps[27 + 49] = [self.cords[0] - 7, self.cords[1] - 7]
                else:
                    self.steps[0 + 49] = [None, None]
                    self.steps[1 + 49] = [None, None]
                    self.steps[2 + 49] = [None, None]
                    self.steps[3 + 49] = [None, None]
                    self.steps[4 + 49] = [None, None]
                    self.steps[5 + 49] = [None, None]
                    self.steps[6 + 49] = [None, None]
                    self.steps[7 + 49] = [None, None]
                    self.steps[8 + 49] = [None, None]
                    self.steps[9 + 49] = [None, None]
                    self.steps[10 + 49] = [None, None]
                    self.steps[11 + 49] = [None, None]
                    self.steps[12 + 49] = [None, None]
                    self.steps[13 + 49] = [None, None]
                    self.steps[14 + 49] = [None, None]
                    self.steps[15 + 49] = [None, None]
                    self.steps[16 + 49] = [None, None]
                    self.steps[17 + 49] = [None, None]
                    self.steps[18 + 49] = [None, None]
                    self.steps[19 + 49] = [None, None]
                    self.steps[20 + 49] = [None, None]
                    self.steps[21 + 49] = [None, None]
                    self.steps[22 + 49] = [None, None]
                    self.steps[23 + 49] = [None, None]
                    self.steps[24 + 49] = [None, None]
                    self.steps[25 + 49] = [None, None]
                    self.steps[26 + 49] = [None, None]
                    self.steps[27 + 49] = [None, None]
                if "ZigZag" in list_of_types:
                    self.steps[0 + 77] = [self.cords[0] + 1, self.cords[1]]
                    self.steps[1 + 77] = [self.cords[0] + 2, self.cords[1]]
                    self.steps[2 + 77] = [self.cords[0] + 3, self.cords[1]]
                    self.steps[3 + 77] = [self.cords[0] + 4, self.cords[1]]
                    self.steps[4 + 77] = [self.cords[0] + 5, self.cords[1]]
                    self.steps[5 + 77] = [self.cords[0] + 6, self.cords[1]]
                    self.steps[6 + 77] = [self.cords[0] + 7, self.cords[1]]
                    self.steps[7 + 77] = [self.cords[0] - 1, self.cords[1]]
                    self.steps[8 + 77] = [self.cords[0] - 2, self.cords[1]]
                    self.steps[9 + 77] = [self.cords[0] - 3, self.cords[1]]
                    self.steps[10 + 77] = [self.cords[0] - 4, self.cords[1]]
                    self.steps[11 + 77] = [self.cords[0] - 5, self.cords[1]]
                    self.steps[12 + 77] = [self.cords[0] - 6, self.cords[1]]
                    self.steps[13 + 77] = [self.cords[0] - 7, self.cords[1]]
                    self.steps[14 + 77] = [self.cords[0] - 1, self.cords[1] + 1]
                    self.steps[15 + 77] = [self.cords[0] - 2, self.cords[1] + 2]
                    self.steps[16 + 77] = [self.cords[0] - 3, self.cords[1] + 3]
                    self.steps[17 + 77] = [self.cords[0] - 4, self.cords[1] + 4]
                    self.steps[18 + 77] = [self.cords[0] - 5, self.cords[1] + 5]
                    self.steps[19 + 77] = [self.cords[0] - 6, self.cords[1] + 6]
                    self.steps[20 + 77] = [self.cords[0] - 7, self.cords[1] + 7]
                    self.steps[21 + 77] = [self.cords[0] + 1, self.cords[1] - 1]
                    self.steps[22 + 77] = [self.cords[0] + 2, self.cords[1] - 2]
                    self.steps[23 + 77] = [self.cords[0] + 3, self.cords[1] - 3]
                    self.steps[24 + 77] = [self.cords[0] + 4, self.cords[1] - 4]
                    self.steps[25 + 77] = [self.cords[0] + 5, self.cords[1] - 5]
                    self.steps[26 + 77] = [self.cords[0] + 6, self.cords[1] - 6]
                    self.steps[27 + 77] = [self.cords[0] + 7, self.cords[1] - 7]
                else:
                    self.steps[0 + 77] = [None, None]
                    self.steps[1 + 77] = [None, None]
                    self.steps[2 + 77] = [None, None]
                    self.steps[3 + 77] = [None, None]
                    self.steps[4 + 77] = [None, None]
                    self.steps[5 + 77] = [None, None]
                    self.steps[6 + 77] = [None, None]
                    self.steps[7 + 77] = [None, None]
                    self.steps[8 + 77] = [None, None]
                    self.steps[9 + 77] = [None, None]
                    self.steps[10 + 77] = [None, None]
                    self.steps[11 + 77] = [None, None]
                    self.steps[12 + 77] = [None, None]
                    self.steps[13 + 77] = [None, None]
                    self.steps[14 + 77] = [None, None]
                    self.steps[15 + 77] = [None, None]
                    self.steps[16 + 77] = [None, None]
                    self.steps[17 + 77] = [None, None]
                    self.steps[18 + 77] = [None, None]
                    self.steps[19 + 77] = [None, None]
                    self.steps[20 + 77] = [None, None]
                    self.steps[21 + 77] = [None, None]
                    self.steps[22 + 77] = [None, None]
                    self.steps[23 + 77] = [None, None]
                    self.steps[24 + 77] = [None, None]
                    self.steps[25 + 77] = [None, None]
                    self.steps[26 + 77] = [None, None]
                    self.steps[27 + 77] = [None, None]
                if "ZigZig" in list_of_types:
                    self.steps[0 + 105] = [self.cords[0] + 1, self.cords[1]]
                    self.steps[1 + 105] = [self.cords[0] + 2, self.cords[1]]
                    self.steps[2 + 105] = [self.cords[0] + 3, self.cords[1]]
                    self.steps[3 + 105] = [self.cords[0] + 4, self.cords[1]]
                    self.steps[4 + 105] = [self.cords[0] + 5, self.cords[1]]
                    self.steps[5 + 105] = [self.cords[0] + 6, self.cords[1]]
                    self.steps[6 + 105] = [self.cords[0] + 7, self.cords[1]]
                    self.steps[7 + 105] = [self.cords[0] - 1, self.cords[1]]
                    self.steps[8 + 105] = [self.cords[0] - 2, self.cords[1]]
                    self.steps[9 + 105] = [self.cords[0] - 3, self.cords[1]]
                    self.steps[10 + 105] = [self.cords[0] - 4, self.cords[1]]
                    self.steps[11 + 105] = [self.cords[0] - 5, self.cords[1]]
                    self.steps[12 + 105] = [self.cords[0] - 6, self.cords[1]]
                    self.steps[13 + 105] = [self.cords[0] - 7, self.cords[1]]
                    self.steps[14 + 105] = [self.cords[0] + 1, self.cords[1] + 1]
                    self.steps[15 + 105] = [self.cords[0] + 2, self.cords[1] + 2]
                    self.steps[16 + 105] = [self.cords[0] + 3, self.cords[1] + 3]
                    self.steps[17 + 105] = [self.cords[0] + 4, self.cords[1] + 4]
                    self.steps[18 + 105] = [self.cords[0] + 5, self.cords[1] + 5]
                    self.steps[19 + 105] = [self.cords[0] + 6, self.cords[1] + 6]
                    self.steps[20 + 105] = [self.cords[0] + 7, self.cords[1] + 7]
                    self.steps[21 + 105] = [self.cords[0] - 1, self.cords[1] - 1]
                    self.steps[22 + 105] = [self.cords[0] - 2, self.cords[1] - 2]
                    self.steps[23 + 105] = [self.cords[0] - 3, self.cords[1] - 3]
                    self.steps[24 + 105] = [self.cords[0] - 4, self.cords[1] - 4]
                    self.steps[25 + 105] = [self.cords[0] - 5, self.cords[1] - 5]
                    self.steps[26 + 105] = [self.cords[0] - 6, self.cords[1] - 6]
                    self.steps[27 + 105] = [self.cords[0] - 7, self.cords[1] - 7]
                else:
                    self.steps[0 + 105] = [None, None]
                    self.steps[1 + 105] = [None, None]
                    self.steps[2 + 105] = [None, None]
                    self.steps[3 + 105] = [None, None]
                    self.steps[4 + 105] = [None, None]
                    self.steps[5 + 105] = [None, None]
                    self.steps[6 + 105] = [None, None]
                    self.steps[7 + 105] = [None, None]
                    self.steps[8 + 105] = [None, None]
                    self.steps[9 + 105] = [None, None]
                    self.steps[10 + 105] = [None, None]
                    self.steps[11 + 105] = [None, None]
                    self.steps[12 + 105] = [None, None]
                    self.steps[13 + 105] = [None, None]
                    self.steps[14 + 105] = [None, None]
                    self.steps[15 + 105] = [None, None]
                    self.steps[16 + 105] = [None, None]
                    self.steps[17 + 105] = [None, None]
                    self.steps[18 + 105] = [None, None]
                    self.steps[19 + 105] = [None, None]
                    self.steps[20 + 105] = [None, None]
                    self.steps[21 + 105] = [None, None]
                    self.steps[22 + 105] = [None, None]
                    self.steps[23 + 105] = [None, None]
                    self.steps[24 + 105] = [None, None]
                    self.steps[25 + 105] = [None, None]
                    self.steps[26 + 105] = [None, None]
                    self.steps[27 + 105] = [None, None]
        return friend_cords

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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("5", friend_cords)
        return friend_cords

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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("6", friend_cords)
        return friend_cords

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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("7", friend_cords)
        return friend_cords

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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("8", friend_cords)
        return friend_cords

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
        friend_cords = friend_cords
        friend_copy = friend_cords
        for i in friend_copy:
            if i[0] in self.steps:
                if [self.tag, self.type] not in i:
                    friend_cords[friend_cords.index(i)].append([self.tag, self.type])
            else:
                if [self.tag, self.type] in i:
                    friend_cords[friend_cords.index(i)].pop(friend_cords[friend_cords.index(i)].index([self.tag, self.type]))
        # print("9", friend_cords)
        return friend_cords

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
