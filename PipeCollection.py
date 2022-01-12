import pygame

from constants import DISPLAY_WIDTH, PIPES_PER_MINUTE
from pipe import Pipe


class PipeCollection:
    def __init__(self):
        self.pipes = []
        self.time = 0
        self.frequency = 60 * 1000 / PIPES_PER_MINUTE

    def update(self):
        self._move_pipes()
        self._remove_pipes()
        self._add_pipes()

    def draw(self, game_display):
        for pipe in self.pipes:
            pipe.draw(game_display)

    def _move_pipes(self):
        for pipe in self.pipes:
            pipe.move()

    def _add_pipes(self):
        if pygame.time.get_ticks() - self.time > self.frequency:
            self.pipes.append(Pipe(DISPLAY_WIDTH))
            self.time = pygame.time.get_ticks()

    def _remove_pipes(self):
        for pipe in self.pipes:
            if pipe.is_offscreen():
                self.pipes.remove(pipe)