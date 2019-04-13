import requests
import urllib.request
from urllib.request import Request,urlopen
import time
from bs4 import BeautifulSoup
from lxml import html
import lxml
from lxml import etree
import sys
import bond as bd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SLEEP_TIME = 0.6

pos = 452435213434534
url = 'https://connect4.gamesolver.org/?pos=' + str(pos)

driver = webdriver.Chrome()
#driver.get("http://www.google.com/")
# Go to your page url
try:
	driver.execute_script("window.open('');")

	driver.get(url)
	# Get button you are going to click by its id ( also you could us find_element_by_css_selector to get element by css selector)
	button_element = driver.find_element_by_id('hide_solution_div')
	button_element.click()
	time.sleep(SLEEP_TIME)
	for i in range(0,6):
		el = driver.find_element_by_xpath('//*[@id="sol' + str(i) + '"]')
		print(el.get_attribute('innerHTML'))
	driver.execute_script("window.close('');")
except Exception as e:
	print(e)
finally:
	driver.quit()
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