from bson import json_util, ObjectId
import datetime
import json
import uuid
import time
import logging
logging.basicConfig(format='%(asctime)s-%(process)d-%(levelname)s-%(message)s', datefmt='%d-%b-%Y %H:%M:%S',level=logging.DEBUG)   # INFO, DEBUG , ERROR ,WARN ,
logger = logging.getLogger(__name__)
logger.info('Start logging -----------------------------')

# selenium Automation Scripts
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions() # define options
options.add_argument("disable-infobars") # disabling infobars
#options.add_argument("--headless") # pass headless argument to the options
options.add_argument("--incognito")
options.add_argument("--disable-extensions") # disabling extensions
#options.desired_capabilities={'loggingPrefs': {'profiler': 'INFO'}}
#driver = webdriver.Firefox(executable_path = 'C:/python-project/firefox/geckodriver.exe')
driver = webdriver.Chrome('C:/python-project/crominum/chrome32bit/chromedriver.exe', chrome_options=options)  # Optional argument, if not specified will search path.
print('Available log types:', driver.execute('getAvailableLogTypes')['value'])
#driver.delete_all_cookies()
target_enviornment = 'https://www.google.com'
driver.get(target_enviornment);

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = (domComplete - responseStart)/1000

logger.debug("Back End Performance : %s" % backendPerformance)
logger.debug("Front End Performance : %s" % frontendPerformance)
f = open("performance.txt","a+")
f.write("%s\r\n" % frontendPerformance)
f.close()
#print('Profiler log:', driver.execute('getLog', {'type': 'performance'})['value'])
#time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
time.sleep(3)
#time.sleep(4)
driver.find_element_by_xpath("xpath=//input[@id='usernameTextBox']").click()
time.sleep(1)

#driver.quit()

driver.get_network_conditions()
driver.save_screenshot()
driver.get_log()
