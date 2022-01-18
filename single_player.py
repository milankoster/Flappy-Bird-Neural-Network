import pygame

from bird import Bird
from constants import *
from game import Game, draw_text, bg_img
from pipe_collection import PipeCollection


class SinglePlayer(Game):

    def __init__(self, title=TITLE):
        super().__init__(title)
        self.bird = Bird(BIRD_STARTER_X, BIRD_STARTER_Y)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self._handle_game_events(self.bird)
            self._update()
            self._draw_window()

            if self.bird.collide(self.pipe_collection):
                self._reset()

    def _draw_window(self):
        self.game_display.blit(bg_img, (0, 0))
        self.pipe_collection.draw(self.game_display)
        self.ground.draw(self.game_display)
        self.bird.draw(self.game_display)

        draw_text(self.game_display, str(self.score), X_SCORE_POS, Y_SCORE_POS, SCORE_FONT, SCORE_SIZE, WHITE)
        pygame.display.update()

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
