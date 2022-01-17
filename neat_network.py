import neat

from bird import Bird
from constants import *
from neat_game import NeatGame

class NeatNetwork:
    def __init__(self, has_reporter):
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                    neat.DefaultSpeciesSet, neat.DefaultStagnation, NEAT_CONFIG)
        self.population = neat.Population(config)

        if has_reporter:
            self.population.add_reporter(neat.StdOutReporter(True))
            self.population.add_reporter(neat.StatisticsReporter())

        self.nets = []
        self.birds = []
        self.gens = []

        self.gen = 0
        self.max_score = 0

    def run(self, generations):
        winner = self.population.run(self.eval_genomes, generations)
        print('\nBest genome:\n{!s}'.format(winner))

    def eval_genomes(self, genomes, config):
        self.gen += 1
        for x, genome in genomes:
            genome.fitness = 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            self.birds.append(Bird(BIRD_STARTER_X, BIRD_STARTER_Y))
            self.nets.append(net)
            self.gens.append(genome)

        neat_game = NeatGame(self.birds, self.nets, self.gens, self.gen, self.max_score, 'Flappy Bird Reinforcement Learning')
        score = neat_game.run_game()
        self.max_score = max(self.max_score, score)

