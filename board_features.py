from connect_4 import *
from c4_scrape import *
import threading as thr

NROWS = 6
NCOLS = 7
FEATURES_FILE = "feed_the_beast.csv"
lock = thr.Lock() # semaphore


def store_features(filename, features_array):
    # Red light
    lock.acquire()
    # Writing file
    f = open(filename, "a")
    f.write(str(features_array)) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
                features_array.append(points[i])
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
                features_array.append(points[i])
                # Writing features in a file
                store_features(FEATURES_FILE, features_array)
