from neat_network import NeatNetwork
from single_player import SinglePlayer

if __name__ == '__main__':
    neat = NeatNetwork(True)
    neat.run(300)
