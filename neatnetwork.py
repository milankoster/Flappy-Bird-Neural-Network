import neat

from bird import Bird
from neatgame import NeatGame


class NeatNetwork:
    def __init__(self, config_path, has_reporter):
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                    neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
        self.population = neat.Population(config)
        if has_reporter:
            self.population.add_reporter(neat.StdOutReporter(True))
            self.population.add_reporter(neat.StatisticsReporter())
        self.gen = 0
        self.nets = []  # TODO Can this be dict?
        self.birds = []
        self.gens = []

    def run(self, generations):
        winner = self.population.run(self.eval_genomes, generations)
        print('\nBest genome:\n{!s}'.format(winner))

    def eval_genomes(self, genomes, config):
        for x, genome in genomes:
            genome.fitness = 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            self.nets.append(net)
            self.birds.append(Bird(230, 350))
            self.gens.append(genome)

        neat_game = NeatGame(self.birds, self.gens)
        neat_game.run_game(30)
