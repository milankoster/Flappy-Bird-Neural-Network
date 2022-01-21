from neat_network import NeatNetwork

if __name__ == '__main__':
    neat = NeatNetwork(True, 100000)
    neat.run(50)
