import pygame
import visualize

from constants import *
from game import Game, draw_text, bg_img
import neat


class NeatGame(Game):
    def __init__(self, birds, nets, genome, gen, max_score, title):
        super().__init__(title)
        self.birds = birds
        self.nets = nets
        self.genome = genome
        self.gen = gen
        self.max_score = max_score

    def visualise_network(self, genome):
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                    neat.DefaultSpeciesSet, neat.DefaultStagnation, NEAT_CONFIG)
        visualize.draw_net(config, genome, view=False)
        # visualize.plot_stats(stats, ylog=False, view=True)
        # visualize.plot_species(stats, view=True)

    def run_game(self):
        while self.running and len(self.birds) > 0:
            self.clock.tick(FPS)
            self._handle_game_events()
            self._update()
            self._draw_window()

            for bird in self.birds:
                if bird.collide(self.pipe_collection):
                    # if len(self.genome) == 1:
                    #     self.visualise_network(self.genome[0])
                    self.nets.pop(self.birds.index(bird))
                    self.genome.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))

        print('Maximum Score Reached:', self.score)
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
        self._update_score()

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
            self.genome[x].fitness += 0.1  # give each bird a fitness of 0.1 for each frame it stays alive
            bird.move()

            # use bird, top pipe and bottom pipe location and determine from network whether to jump or not
            output = self.nets[x].activate(
                (bird.y,
                 abs(self.pipes[pipe_ind].top_height - self.pipes[0].PIPE_TOP.get_height()),
                 abs(self.pipes[pipe_ind].bottom_height)))

            if output[0] > 0:  # tanh activation function result will be between -1 and 1. if over 0.5 jump
                bird.jump()

    def _update_score(self):
        super()._update_score(self.birds[0])
        for genome in self.genome:
            genome.fitness += 5

    def _draw_labels(self):
        label_font = pygame.font.SysFont(LABEL_FONT, LABEL_SIZE)

        # generations
        score_label = label_font.render("Generation: " + str(self.gen), True, WHITE)
        self.game_display.blit(score_label, (10, DISPLAY_HEIGHT - 70))

        # alive
        score_label = label_font.render("Alive: " + str(len(self.birds)), True, WHITE)
        self.game_display.blit(score_label, (10, DISPLAY_HEIGHT - 50))

        # score
        score_label = label_font.render("Max Score: " + str(max(self.max_score, self.score)), True, WHITE)
        self.game_display.blit(score_label, (10, DISPLAY_HEIGHT - 30))
