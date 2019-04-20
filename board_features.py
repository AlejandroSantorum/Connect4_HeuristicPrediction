from connect_4 import *
from c4_scrape import *
import threading as thr

NROWS = 6
NCOLS = 7
FEATURES_FILE = "feed_the_beast.csv"
LEGEND_FILE = "N_PIECES  ALLY_MEAN_DIST  OPP_MEAN_DIST  ALLY_#2_BLCK  ALLY_#2_EFF  OPP_#2_BLCK  OPP_#2_EFF  ALLY_#3_BLCK  ALLY_#3_EFF  OPP_#3_BLCK  OPP_#3_EFF\n"
lock = thr.Lock() # semaphore


def init_features_file():
    f = open(FEATURES_FILE, "a")
    f.write(LEGEND_FILE)
    f.close()


def store_features(filename, features_array):
    # Red light
    lock.acquire()
    # Writing file
    f = open(filename, "a")
    f.write(str(features_array)[1:len(str(features_array))-1])
    f.write("\n")
    f.close()
    # Green light
    lock.release()


def empty_points(points_array):
    for i in range(NCOLS):
        if points_array[i] != '':
            return False
    return True


def features_main(pattern, points_array):
    if empty_points(points_array)==True:
        board = Board(NROWS, NCOLS)
        current_pattern, current_piece = board.build_pattern(pattern)
        points = get_points(current_pattern)
        for i in range(NCOLS):
            if points[i] != '-':
                # Getting child board
                board.insert(current_piece, i)
                # Getting features of this board
                features_array = board.get_features(current_piece)
                # Getting the father state
                board.go_back(i)
                # Adding points
                features_array.append(int(points[i]))
                # Writing features in a file
                store_features(FEATURES_FILE, features_array)

    else:
        board = Board(NROWS, NCOLS)
        current_pattern, current_piece = board.build_pattern(pattern)
        for i in range(NCOLS):
            if points_array[i] != '':
                # Getting child board
                board.insert(current_piece, i)
                # Getting features of this board
                features_array = board.get_features(current_piece)
                # Getting the father state
                board.go_back(i)
                # Adding points
                features_array.append(int(points_array[i]))
                # Writing features in a file
                store_features(FEATURES_FILE, features_array)
