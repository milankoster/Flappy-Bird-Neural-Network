import pygame

from constants import *

bird_img = pygame.image.load(BIRD_FILENAME)


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.rotation = 0
        self.img = bird_img

    def move(self):
        self.y = self.y + self.speed
        self.speed = self.speed + BIRD_GRAVITY
        self._tilt()

    def jump(self):
        if self.y > Y_LIMIT:
            self.speed = BIRD_JUMP_SPEED

    # Tilt the bird up and down based on its vertical speed
    def _tilt(self):
        if self.speed < MIN_ROTATION_GRAVITY:
            if self.rotation < MAX_ROTATION_UP:
                self.rotation += ROT_VEL_INCREASE
                self.rotation = min(self.rotation, MAX_ROTATION_UP)
        else:
            if self.rotation > MAX_ROTATION_DOWN:
                self.rotation -= ROT_VEL_DECREASE

    # Check if bird collides with floor and pipes
    def collide(self, pipe_collection):
        if self.y + self.img.get_rect().height > FLOOR_HEIGHT:  # Check floor
            return True
        if len(pipe_collection.pipes) != 0:  # Check pipes
            pipe = pipe_collection.pipes[0]
            top_collide = self._overlap(pipe.x, pipe.top_height, pipe.PIPE_TOP)
            bottom_collide = self._overlap(pipe.x, pipe.bottom_height, pipe.PIPE_BOTTOM) 
            if top_collide or bottom_collide:
                return True
            return top_collide or bottom_collide

    def _overlap(self, x, y, img):
        bird_mask = pygame.mask.from_surface(self.img)
        mask = pygame.mask.from_surface(img)
        offset = (x - self.x, y - round(self.y))
        return bird_mask.overlap(mask, offset)

    # Draw the bird based on its tilt
    def draw(self, win):
        rotated_image = pygame.transform.rotate(bird_img, self.rotation)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
        self.img = rotated_image

