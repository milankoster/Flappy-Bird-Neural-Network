import pygame

from constants import DISPLAY_WIDTH, PIPE_WIDTH_GAP, PIPE_STARTER_X
from pipe import Pipe


class PipeCollection:
    def __init__(self):
        self.pipes = [Pipe(PIPE_STARTER_X)]
        self.time = 0

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
        if DISPLAY_WIDTH - PIPE_WIDTH_GAP > self.pipes[-1].x:
            self.pipes.append(Pipe(DISPLAY_WIDTH))
            self.time = pygame.time.get_ticks()

    def _remove_pipes(self):
        for pipe in self.pipes:
            if pipe.is_offscreen():
                self.pipes.remove(pipe)