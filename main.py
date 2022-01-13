from game import Game
from neatgame import NeatGame
import os

from neatnetwork import NeatNetwork

if __name__ == '__main__':
    # game = Game()
    # game.run_game()

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    neat = NeatNetwork(config_path, True)
