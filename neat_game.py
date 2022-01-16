import pygame

from constants import *
from game import Game


class NeatGame(Game):
    def __init__(self, birds, nets, genome, title):
        super().__init__(title)
        self.birds = birds
        self.nets = nets
        self.genome = genome

    def run_game(self):
        while self.running and len(self.birds) > 0:
            self.clock.tick(FPS)
            self._handle_game_events()
            self._update()
            self._draw_window()

            for bird in self.birds:
                if bird.collide(self.pipe_collection):
                    self.genome[self.birds.index(bird)].fitness -= 1
                    self.nets.pop(self.birds.index(bird))
                    self.genome.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))

    def _handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                quit()
                break

    def _update(self):
        self._update_birds()
        self.ground.move()
        self.pipe_collection.update()
        self._update_score(self.birds[0])

    def _update_birds(self):
        pipe_ind = 0
        if len(self.birds) > 0:
            if self.birds[0].x > self.pipes[0].x + self.pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1

        for x, bird in enumerate(self.birds):
            self.genome[x].fitness += 0.1  # give each bird a fitness of 0.1 for each frame it stays alive
            bird.move()

            # use bird, top pipe and bottom pipe location and determine from network whether to jump or not
            output = self.nets[x].activate(
                (bird.y,
                 abs(self.pipes[pipe_ind].top_height - self.pipes[0].PIPE_TOP.get_height()),
                 abs(self.pipes[pipe_ind].bottom_height)))

            if output[0] > 0:  # tanh activation function result will be between -1 and 1. if over 0.5 jump
                bird.jump()

    def _draw_bird(self):
        for bird in self.birds:
            bird.draw(self.game_display)
