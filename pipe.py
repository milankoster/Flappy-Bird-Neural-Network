import pygame
import random

from constants import *

pipe_img = pygame.image.load(PIPE_FILENAME)


class Pipe:
    def __init__(self, x):
        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)  # Flip vertically
        self.PIPE_BOTTOM = pipe_img
        self.x = x
        self.top_height, self.bottom_height = self._set_height()
        self.passed = False

    # Set the height of a pipe
    def _set_height(self):
        height = random.randrange(PIPE_MIN_HEIGHT, PIPE_MAX_HEIGHT)
        top = height - self.PIPE_TOP.get_height()
        bottom = height + PIPE_GAP
        return top, bottom

    # Move pipe to the left based on constant velocity
    def move(self):
        self.x -= PIPE_VELOCITY

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top_height))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom_height))

    def is_offscreen(self):
        return self.x + self.PIPE_TOP.get_rect().width < 0