import pygame

from constants import FLOOR_VELOCITY, BASE_FILENAME


class Base:

    def __init__(self, y):
        self.img = pygame.image.load(BASE_FILENAME)
        self.width = self.img.get_width()
        self.y = y
        self.x1 = 0
        self.x2 = self.img.get_width()

    # Move both floor object to the left
    def move(self):
        self.x1 -= FLOOR_VELOCITY
        self.x2 -= FLOOR_VELOCITY

        # Move floor when off the screen
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width
        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    # Draw the floor consisting of two images
    def draw(self, win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))
