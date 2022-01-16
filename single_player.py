import pygame

from bird import Bird
from constants import *
from game import Game
from pipe_collection import PipeCollection


class SinglePlayer(Game):

    def __init__(self, title):
        super().__init__(title)
        self.bird = Bird(BIRD_STARTER_X, BIRD_STARTER_Y)

    def run_game(self):
        while self.running:
            self.clock.tick(FPS)
            self._handle_game_events(self.bird)
            self._update()
            self._draw_window()

            if self.bird.collide(self.pipe_collection):
                self._reset()

    def _handle_game_events(self, bird):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

    def _update(self):
        self.bird.move()
        self.ground.move()
        self.pipe_collection.update()
        self._update_score(self.bird)

    def _reset(self):
        self.pipe_collection = PipeCollection()
        self.bird = Bird(BIRD_STARTER_X, BIRD_STARTER_Y)
        self.score = 0

    def _draw_bird(self):
        self.bird.draw(self.game_display)
