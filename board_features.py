from connect4 import *
from c4_scrape import *

NROWS = 6
NCOLS = 7

def empty_points(array_points):
    for i in range(NCOLS):
        if array_points[i] != '':
            return False
    return True

def calculate_child_features(pattern, array_points):
    if empty_points(array_points)==True:
        board = Board(NROWS, NCOLS)
        current_pattern, current_piece = board.build_pattern(pattern)
        points = get_points(current_pattern)
        # For each point != '-' board.insert(col_index) + board.features() + board.goback
        # Write in a file (semaphore!!)
    else:
        # For each point != '-' board.insert(col_index) + board.features() + board.goback
        # Write in a file (semaphore!!)
