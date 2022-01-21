# General Game Information
TITLE = 'Flappy Bird'
TRAIN_TITLE = 'Flappy Bird Reinforcement Learning'
DISPLAY_WIDTH = 315
DISPLAY_HEIGHT = 560
FPS = 120
Y_LIMIT = 10

# Score
X_SCORE_POS = int(DISPLAY_WIDTH / 2)
Y_SCORE_POS = 20
SCORE_FONT = 'Bauhaus 93'
SCORE_SIZE = 60
WHITE = (255, 255, 255)

# Labels
LABEL_FONT = 'Raleway'
LABEL_SIZE = 24


# Files
BASE_FILENAME = '../Flappy Bird Reinforcement Learning/images/base.png'
PIPE_FILENAME = '../Flappy Bird Reinforcement Learning/images/pipe.png'
BIRD_FILENAME = '../Flappy Bird Reinforcement Learning/images/Flappy.png'
BACKGROUND_FILENAME = '../Flappy Bird Reinforcement Learning/images/bg.png'
NEAT_CONFIG = 'config-feedforward.txt'

# Ground Info
FLOOR_HEIGHT = 450
FLOOR_VELOCITY = 1.1


# Pipe Info
PIPE_STARTER_X = 500
PIPE_SCALE = 1.12

PIPE_VELOCITY = FLOOR_VELOCITY
PIPE_GAP = 110
PIPE_WIDTH_GAP = 175
PIPE_MIN_HEIGHT = 80
PIPE_MAX_HEIGHT = FLOOR_HEIGHT - PIPE_GAP - 100


# Bird Info
BIRD_STARTER_X = 60
BIRD_STARTER_Y = 250

BIRD_JUMP_SPEED = -2.6
BIRD_GRAVITY = 0.065

MIN_ROTATION_GRAVITY = 2
MAX_ROTATION_UP = 25
MAX_ROTATION_DOWN = -90
ROT_VEL_INCREASE = 5
ROT_VEL_DECREASE = 2