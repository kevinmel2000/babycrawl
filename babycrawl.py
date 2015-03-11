#!/bin/python
"""Usage: 
	babycrawl.py [--debug] <url>
	babycrawl.py -h | --help
	babycrawl.py --version

Arguments:
	<url>    web url to use for clicking
	
Options:
	-h --help            show this
	--debug              shows browser window
	--version            shows the current version
"""
from docopt import docopt
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import time
from pyvirtualdisplay import Display

urlhistory=[]

def runapp(url, close_Window):
	driver = webdriver.Firefox()
	
	driver.get(url)
	wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
	
	
	
	allelements = driver.find_elements_by_xpath('//*')
	total_element_count=len(allelements)
	print '+++found ' + str(total_element_count)+' elements'
	
	currentelement=0;
	
	# our ending url may be different from the one we started with.
	
	settledurl = driver.current_url
	print '+++settled on '+settledurl
	for element in allelements:
		clickelement(driver, settledurl, currentelement)
		currentelement+=1
	
	if close_Window == True:
		driver.quit()

def clickelement(webdriver, url, element_index):
	currenturl = webdriver.current_url
	reopenurl=True
	check1 = currenturl.replace(url, '')
	if check1 == '':
		reopenurl=False
	
	if reopenurl:
		logUrl(currenturl)
		webdriver.get(url)
		wait = ui.WebDriverWait(webdriver, 10) # timeout after 10 seconds
	
	try:
		allelements = webdriver.find_elements_by_xpath('//*')
		allelements[element_index].click()
	except:
		pass

def logUrl(url):
	if url not in urlhistory:
		print url
		urlhistory.append(url)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='babycrawl 2.2')
    url = arguments['<url>']
    debug = arguments['--debug']
    display=''
    if debug == False:
		# hide the window unless in debug mode
		display = Display(visible=0, size=(1920, 1080))
		display.start()
	
    closewindow=debug==False
    runapp(url, closewindow)
    
    if debug == False:
		display.stop()
	

