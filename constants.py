"""
List of constants for the game
"""
from pygame import Color
SF = 2  # Scaling factor for hidpi monitors

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RETRO_VIOLET = Color('#180f23')
RETRO_PINK = Color('#fc2481')
RETRO_BLUE = Color("#00ffff")
NEON_YELLOW = Color("#ffff00")
#
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 30
# Cube size is cell size minus width of 2 lines, which is 2*SF
CUBE_SIZE = CELL_SIZE - 2 * SF

IMPEDANCE = 30
