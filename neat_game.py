import pygame

from constants import *
from game import Game, draw_text, bg_img


class NeatGame(Game):
    def __init__(self, birds, nets, genome, gen, max_score, score_aim, title):
        super().__init__(title)
        self.birds = birds
        self.nets = nets
        self.genome = genome
        self.gen = gen
        self.max_score = max_score
        self.score_aim = score_aim

    def run(self):
        while self.running and len(self.birds) > 0:
            self.clock.tick(FPS)
            self._handle_game_events()
            self._update()
            self._draw_window()

            for bird in self.birds:
                if bird.collide(self.pipe_collection):
                    self.nets.pop(self.birds.index(bird))
                    self.genome.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))
            if self.score >= self.score_aim:
                # for genome in self.genome:
                #     genome.fitness += 1000000
                return self.score

        print('Score Reached:', self.score)
        return self.score

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

    def _draw_window(self):
        self.game_display.blit(bg_img, (0, 0))
        self.pipe_collection.draw(self.game_display)
        self.ground.draw(self.game_display)
        for bird in self.birds:
            bird.draw(self.game_display)
        self._draw_labels()

        draw_text(self.game_display, str(self.score), X_SCORE_POS, Y_SCORE_POS, SCORE_FONT, SCORE_SIZE, WHITE)
        pygame.display.update()

    def _update_birds(self):
        pipe_ind = 0
        if len(self.birds) > 0:
            if self.birds[0].x > self.pipes[0].x + self.pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1

        for x, bird in enumerate(self.birds):
            self.genome[x].fitness += 0.01  # give each bird a fitness of 0.1 for each frame it stays alive
            bird.move()

            # use bird, top pipe and bottom pipe location and determine from network whether to jump or not
            output = self.nets[x].activate(
                (bird.y,
                 abs(self.pipes[pipe_ind].top_height - self.pipes[0].PIPE_TOP.get_height()),
                 abs(self.pipes[pipe_ind].bottom_height)))

            if output[0] > 0:  # tanh activation function result will be between -1 and 1. if over 0.5 jump
                bird.jump()

    def _update_score(self, bird):
        if super()._update_score(bird):
            for genome in self.genome:
                genome.fitness += 5

    def _draw_labels(self):
        label_font = pygame.font.SysFont(LABEL_FONT, LABEL_SIZE)

        # generations
        label = label_font.render("Generation: " + str(self.gen), True, WHITE)
        self.game_display.blit(label, (10, DISPLAY_HEIGHT - 70))

        # alive
        label = label_font.render("Alive: " + str(len(self.birds)), True, WHITE)
        self.game_display.blit(label, (10, DISPLAY_HEIGHT - 50))

        # score
        label = label_font.render("Max Score: " + str(max(self.max_score, self.score)), True, WHITE)
        self.game_display.blit(label, (10, DISPLAY_HEIGHT - 30))
