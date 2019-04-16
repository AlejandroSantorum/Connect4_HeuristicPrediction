import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SLEEP_TIME = 0.65
MAIN_URL = 'https://connect4.gamesolver.org/?pos='

PIECES = ["1", "1", "1", "1", "1", "1",
		  "2", "2", "2", "2", "2", "2",
		  "3", "3", "3", "3", "3", "3",
		  "4", "4", "4", "4", "4", "4",
		  "5", "5", "5", "5", "5", "5",
		  "6", "6", "6", "6", "6", "6",
		  "7", "7", "7", "7", "7", "7"]

MAX_PIECES = 41
MAX_PLAYS = 35
MIN_PLAYS = 5


def generate_board():
	board = ""
	n_plays = randint(MIN_PLAYS, MAX_PLAYS)
	for i in range(n_plays):
		pos = randint(0,MAX_PIECES-i)
		board += PIECES[pos]
	return board


def scrape_main(n_examples):
	first_pos = generate_board()
	first_url = MAIN_URL + first_pos

	#######################################
	# delete print later
	print(first_pos)
	#######################################

	# Initializing webdriver (Chrome in this case)
	driver = webdriver.Chrome()

	# Opening it for the first time
	driver.get(first_url)

	try:
		for i in range(n_examples):
			# Opening a new tab to use it later
			next_tab = "tab"+str(i+1)
			new_tab_command = "window.open('about:blank', \'"+next_tab+"\');"
			driver.execute_script(new_tab_command)

			# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
			button_element = driver.find_element_by_id('hide_solution_div')

			# Getting points
			time.sleep(SLEEP_TIME)
			for j in range(0,7):
				el = driver.find_element_by_xpath('//*[@id="sol' + str(j) + '"]')
				#######################################
				# delete print later
				print(el.get_attribute('innerHTML'))

			# Closing current tab
			driver.close()

			# Switching tabs
			driver.switch_to.window(next_tab)

			# Random URL generator soon...
			board = generate_board()
			#######################################
			# delete print later
			print(board)
			#######################################
			next_url = MAIN_URL+board
			driver.get(next_url)

	except Exception as err:
		print("Something went wrong at iteration: "+str(i)+" ==> " + str(err))
	finally:
		driver.quit()
		return


M = 10
if __name__ == "__main__":
	scrape_main(M)


