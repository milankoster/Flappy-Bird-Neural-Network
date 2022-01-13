﻿# General Game Information
TITLE = 'Flappy Bird'
DISPLAY_WIDTH = 315
DISPLAY_HEIGHT = 560
FPS = 120

# Game
Y_LIMIT = 10

# Score
X_SCORE = int(DISPLAY_WIDTH / 2)
Y_SCORE = 20
SCORE_FONT = 'Bauhaus 93'
SCORE_SIZE = 60
WHITE = (255, 255, 255)



# Files
BASE_FILENAME = 'images/base.png'
PIPE_FILENAME = 'images/pipe.png'
BIRD_FILENAME = 'images/bird1.png'
BACKGROUND_FILENAME = 'images/bg.png'

# Ground Info
FLOOR_HEIGHT = 450
FLOOR_VELOCITY = 1.1
# FLOOR_VELOCITY = 1.1 * (DT / 120)


# Pipe Info
PIPE_VELOCITY = FLOOR_VELOCITY
PIPE_GAP = 100
PIPE_MIN_HEIGHT = 80
PIPE_MAX_HEIGHT = FLOOR_HEIGHT - PIPE_GAP - 100
PIPES_PER_MINUTE = 45
# PIPES_PER_MINUTE = 45 * (DT / 120)


# Bird Info
BIRD_JUMP_SPEED = -2.6
BIRD_GRAVITY = 0.07
MIN_ROTATION_GRAVITY = 2
MAX_ROTATION_UP = 25
MAX_ROTATION_DOWN = -90
ROT_VEL_INCREASE = 5
ROT_VEL_DECREASE = 2
BIRD_STARTER_X = 60
BIRD_STARTER_Y = 250