################################################################################
#   Authors:                                                                   #
#       · Alejandro Santorum Varela - alejandro.santorum@estudiante.uam.es     #
#                                     alejandro.santorum@gmail.com             #
#   Date: Apr 14, 2019                                                         #
#   File: c4_scrape.py                                                         #
#   Project: Connect4 - Predicting heuristic values                            #
#   Version: 1.1                                                               #
################################################################################
import time
import sys
import threading as thr
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from board_features import *


SLEEP_TIME = 0.7
MAIN_URL = 'https://connect4.gamesolver.org/?pos='

PIECES = ["1", "1", "1", "1", "1", "1",
		  "2", "2", "2", "2", "2", "2",
		  "3", "3", "3", "3", "3", "3",
		  "4", "4", "4", "4", "4", "4",
		  "5", "5", "5", "5", "5", "5",
		  "6", "6", "6", "6", "6", "6",
		  "7", "7", "7", "7", "7", "7"]

MAX_PIECES = 42 # Maximum number of pieces on a Connect4 board
MAX_PLAYS = 35  # Maximum number of plays
MIN_PLAYS = 5   # Minimum number of plays

################################################################
#	It generates a random board pattern. The pattern length is
#	chosen randomly between MIN_PLAYS and MAX_PLAYS, and the
#	played column in each turn is also chosen randomly
################################################################
def generate_board_pattern():
	board = ""
	# Auxiliary pieces array
	pieces_aux = PIECES.copy()
	# Getting randomly the number of plays
	n_plays = randint(MIN_PLAYS, MAX_PLAYS)
	for i in range(n_plays):
		# Getting random piece position
		pos = randint(0,MAX_PIECES-i-1)
		# Extracting piece and adding it to the board pattern expression
		board += pieces_aux.pop(pos)
	return board


################################################################
#	It creates a webdriver (in this case ChromeDriver) and loops
#	'n_examples' times, getting a random board pattern, search it
#	and starting a parallel thread that will calculate the desired
#	board features (storing them in a file)
################################################################
def scrape_main(n_examples):
	start_time = time.time()

	# Getting init board pattern
	pattern = generate_board_pattern()
	first_url = MAIN_URL + pattern

	# Initializing webdriver (Chrome in this case)
	driver = webdriver.Chrome()
	# Opening it for the first time
	driver.get(first_url)

	try:
		# Main loop
		for i in range(n_examples):
			print("N example: ", i)
			# Opening a new tab to use it later
			next_tab = "tab"+str(i+1)
			new_tab_command = "window.open('about:blank', \'"+next_tab+"\');"
			driver.execute_script(new_tab_command)

			# Get button you are going to click by its id (also you could
			# find_element_by_css_selector to get element by css selector)
			button_element = driver.find_element_by_id('hide_solution_div')

			# Getting points
			time.sleep(SLEEP_TIME)
			points_array = []
			for j in range(0,7):
				elem = driver.find_element_by_xpath('//*[@id="sol' + str(j) + '"]')
				points_array.append(elem.get_attribute('innerHTML'))

			# Creating a new thread to calculate and store features
			features_thread = thr.Thread(
				target = features_main,
				args = (pattern, points_array,)
			)
			features_thread.start()

			# Closing current tab
			driver.close()

			# Switching tabs
			driver.switch_to.window(next_tab)

			# Random URL generator
			pattern = generate_board_pattern()

			next_url = MAIN_URL+pattern
			driver.get(next_url)
		return n_examples
	except Exception as err:
		print("Something went wrong at iteration: "+str(i)+" ==> " + str(err))
		return i
	finally:
		driver.quit()
		end_time = time.time()
		print("Time used: "+str(end_time - start_time)+" seconds")


################################################################
#	This function gets the array of points given a pattern.
#	It is usually used when the status of the table is just
#	previous to a winner movement
################################################################
def get_points(pattern):
	try:
		points = []
		# Preparing url
		url = MAIN_URL+pattern
		# Initializing webdriver (Chrome in this case)
		driver = webdriver.Chrome()
		# Opening it for the first time
		driver.get(url)
		# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
		button_element = driver.find_element_by_id('hide_solution_div')
		# Getting points
		time.sleep(SLEEP_TIME)
		for j in range(0,7):
			el = driver.find_element_by_xpath('//*[@id="sol' + str(j) + '"]')
			#######################################
			# delete print later
			elem = el.get_attribute('innerHTML')
			if elem == '':
				points.append("-")
			else:
				points.append(elem)
		driver.close()
		return points
	except Exception as err:
		print("Something went wrong getting points of a finished board: ", err)
	finally:
		driver.quit()


if __name__ == "__main__":
	# Number of desired examples
	M = 20000
	# Writing header file (features names)
	init_features_file()
	# Preparing counters in error case
	exec_times = 0
	aux_counter = M
	while aux_counter > 0:
		ret = scrape_main(aux_counter)
		exec_times += 1
		print("Return from scrape_main (time "+str(exec_times)+"): "+str(ret))
		aux_counter -= ret
