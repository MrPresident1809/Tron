import pygame
import neat
import time
import os
import random
pygame.font.init()
windowWidth = 800
windowHeight = 800

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

win = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()
filledTiles = []
class Bike:
    def __init__(self, x, y, color, up, down, left, right ):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = color
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.vel = 20
        self.direction = "right"
        self.alive = True
        self.position = (self.x, self.y)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[self.up]:
            self.direction = "up"

        if keys[self.down]:
            self.direction = "down"

        if keys[self.left]:
            self.direction = "left"

        if keys[self.right]:
            self.direction = "right"

        if self.direction == "up":
            self.y -= self.vel
        if self.direction == "down":
            self.y += self.vel
        if self.direction == "left":
            self.x -= self.vel
        if self.direction == "right":
            self.x += self.vel

        self.position = (self.x, self.y)
        #self.path.append(self.position)
        filledTiles.append(self.position)

    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def collide(self):
        for point in filledTiles:
            if point == self.position:
                print(point, self.position)
                self.alive = False


def drawWindow(players):
    for player in players:
        player.move()
        player.draw()
    pygame.display.update()

players = []
player1 = Bike(200, 200, red, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
players.append(player1)
run = True
while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
            break

        for player in players:
            player.collide()
            if player.alive == False:
                print("s")
                #players.remove(player)

    drawWindow(players)
    #print(player1.path)
    print(player1.alive)
    #win.fill(black)