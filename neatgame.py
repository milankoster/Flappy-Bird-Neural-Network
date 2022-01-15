import pygame

from pipe_collection import PipeCollection
from bird import Bird
from constants import *
from ground import Base

bg_img = pygame.image.load(BACKGROUND_FILENAME)
bg_img = pygame.transform.scale(bg_img, (DISPLAY_WIDTH, DISPLAY_HEIGHT))


class NeatGame:
    def __init__(self, birds, nets, genome):
        pygame.init()
        pygame.display.set_caption(TITLE)  # TODO Custom Title

        self.score = 0
        self.running = True
        self.clock = pygame.time.Clock()
        self.ground = Base(FLOOR_HEIGHT)
        self.pipe_collection = PipeCollection()
        self.pipes = self.pipe_collection.pipes
        self.game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.birds = birds
        self.nets = nets
        self.genome = genome

    def run_game(self, generation):
        generation += 1

        # Use Game loop and tick it at FPS count (30)
        while self.running and len(self.birds) > 0:
            self.clock.tick(FPS)
            self._handle_game_events()
            self._update(self.birds)
            self._draw_window(self.birds)

            for bird in self.birds:
                if bird.collide(self.pipe_collection):
                    # self.genome[self.birds.index(bird)].fitness -= 1
                    self.nets.pop(self.birds.index(bird))
                    self.genome.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))

    def _update(self, birds):
        pipe_ind = 0
        if len(birds) > 0:
            if len(self.pipes) > 1 and birds[0].x > self.pipes[0].x + self.pipes[
                0].PIPE_TOP.get_width():  # determine whether to use the first or second
                pipe_ind = 1

        for x, bird in enumerate(birds):
            self.genome[x].fitness += 0.1  # give each bird a fitness of 0.1 for each frame it stays alive
            bird.move()

            # send bird location, top pipe location and bottom pipe location and determine from network whether to jump or not
            pipes = self.pipe_collection.pipes

            if len(pipes) > 0:
                output = self.nets[birds.index(bird)].activate(
                    (bird.y, abs(pipes[pipe_ind].top_height - pipes[0].PIPE_TOP.get_height()), abs(pipes[pipe_ind].bottom_height)))
            else:
                output = self.nets[birds.index(bird)].activate(
                    (bird.y, -1000, -1000))

            if output[0] > 0.5:  # we use a tanh activation function so result will be between -1 and 1. if over 0.5 jump
                bird.jump()

        self.ground.move()
        self.pipe_collection.update()
        self._update_score(birds[0])

    def _update_score(self, bird):
        if len(self.pipe_collection.pipes) > 0:
            pipe = self.pipe_collection.pipes[0]
            if bird.x > pipe.x and not pipe.passed:
                pipe.passed = True
                self.score += 1
                for genome in self.genome:
                    genome.fitness += 5

    def _draw_window(self, birds):
        self.game_display.blit(bg_img, (0, 0))

        self.pipe_collection.draw(self.game_display)
        self.ground.draw(self.game_display)
        for bird in birds:
            bird.draw(self.game_display)

        draw_text(self.game_display, str(self.score), X_SCORE_POS, Y_SCORE_POS, SCORE_FONT, SCORE_SIZE, WHITE)

        pygame.display.update()

    def _handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                quit()
                break


def draw_text(screen, text, x, y, font, size, white):
    font = pygame.font.SysFont(font, size)
    img = font.render(text, True, white)
    screen.blit(img, (x - img.get_width() / 2, y))
