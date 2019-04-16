#######################################################
# USELESS IMPORTS
#######################################################
#import requests
#import urllib.request
#from urllib.request import Request,urlopen
#from bs4 import BeautifulSoup
#from lxml import html
#import lxml
#from lxml import etree
#import sys
#import bond as bd
#from datetime import datetime
#######################################################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


M = 10
SLEEP_TIME = 0.6

pos = 452435213434534
first_url = 'https://connect4.gamesolver.org/?pos=' + str(pos)


# Initializing webdriver (Chrome in this case)
driver = webdriver.Chrome()

# Opening it for the first time
driver.get(first_url)

try:
	for i in range(M):
		# Opening a new tab to use it later
		new_tab_command = "window.open('about:blank', 'tab"+str(i+1)+"\');"
		driver.execute_script(new_tab_command)

		# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
		button_element = driver.find_element_by_id('hide_solution_div')

		# Getting points
		time.sleep(SLEEP_TIME)
		for j in range(0,6):
			el = driver.find_element_by_xpath('//*[@id="sol' + str(j) + '"]')
			print(el.get_attribute('innerHTML'))

		# Closing current tab
		driver.close()

		# Switching tabs
		next_tab = "tab"+str(i+1)
		driver.switch_to.window(next_tab)

		# Random URL generator soon...
		driver.get(first_url)

except Exception as err:
	print("Something went wrong at iteration: "+str(i)+" ==> " + str(err))
finally:
	driver.quit()



###############################################################################
# FIRST SCRATCH

#driver = webdriver.Chrome()
#driver.get("http://www.google.com/")
# Go to your page url
#try:
#	driver.get(url)
#	driver.execute_script("window.open('about:blank', 'tab2');")
	# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
#	button_element = driver.find_element_by_id('hide_solution_div')
#	button_element.click()
#	time.sleep(SLEEP_TIME)
#	for i in range(0,6):
#		el = driver.find_element_by_xpath('//*[@id="sol' + str(i) + '"]')
#		print(el.get_attribute('innerHTML'))
	#driver.execute_script("window.close('');")
#	driver.close()
#except Exception as e:
#	print(e)
#finally:
#	driver.quit()


###############################################################################
# USELESS CODE (?)

#lxml
'''
page = requests.get(url)
page2 = page = requests.get(url,json)
'''
#jresponse = page
#print(jresponse.text)
'''
tree = html.fromstring(page.content)
#el = tree.xpath('/div#sol0.solution.col0')
#print(lxml.html.tostring(el[0]))
for i in range(0,6):
	element = tree.xpath('//*[@id="sol' + str(i) +'"]/text()')
	print(element)

#beautifulsoup


from bs4 import Comment

html = BeautifulSoup(page.content, 'html.parser')
msgDiv = html.find_all('div')
for obj in msgDiv:
	print(obj)'''
###############################################################################