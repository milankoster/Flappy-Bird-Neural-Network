import pygame

from pipe_collection import PipeCollection
from constants import *
from ground import Base
from abc import ABC, abstractmethod

bg_img = pygame.image.load(BACKGROUND_FILENAME)
bg_img = pygame.transform.scale(bg_img, (DISPLAY_WIDTH, DISPLAY_HEIGHT)) 


class Game(ABC):
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)

        self.score = 0
        self.running = True
        self.clock = pygame.time.Clock()

        self.ground = Base(FLOOR_HEIGHT)
        self.pipe_collection = PipeCollection()
        self.pipes = self.pipe_collection.pipes
        self.game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    def _draw_window(self):
        self.game_display.blit(bg_img, (0, 0))
        self.pipe_collection.draw(self.game_display)
        self.ground.draw(self.game_display)
        self._draw_bird()

        draw_text(self.game_display, str(self.score), X_SCORE_POS, Y_SCORE_POS, SCORE_FONT, SCORE_SIZE, WHITE)
        pygame.display.update()

    def _update_score(self, bird):
        if len(self.pipes) > 0:
            pipe = self.pipes[0]
            if bird.x > pipe.x and not pipe.passed:
                pipe.passed = True
                self.score += 1
                return True

    @abstractmethod
    def _draw_bird(self):
        pass


def draw_text(screen, text, x, y, font, size, white):
    font = pygame.font.SysFont(font, size)
    img = font.render(text, True, white)
    screen.blit(img, (x - img.get_width() / 2, y))
