from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import unittest
import datetime
import json
import uuid
import time
import logging
logging.basicConfig(format='%(asctime)s-%(process)d-%(levelname)s-%(message)s', datefmt='%d-%b-%Y %H:%M:%S',level=logging.DEBUG)   # INFO, DEBUG , ERROR ,WARN ,
logger = logging.getLogger(__name__)
logger.info('Start logging -----------------------------')
# import allure
driver = webdriver.Chrome('./chromedriver')
options = webdriver.ChromeOptions() # define options
options.add_argument("disable-infobars") # disabling infobars
#options.add_argument("--headless") # pass headless argument to the options
# options.add_argument("--incognito")
options.add_argument("--disable-extensions") # disabling extensions
#driver.delete_all_cookies()
driver.maximize_window()

Target_env = "https://localhost:3005/app/myapi"

try: 
  driver.get(Target_env)
  logger.info(driver.title)
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
  logger.info(driver.current_url)
  time.sleep(5)
#   driver.refresh()

  driver.find_element(By.ID, "usernameTextBox").send_keys("x")
  time.sleep(1)
  driver.find_element(By.ID, "lp1-next-btn").click()
  time.sleep(2)
  driver.find_element(By.ID, "passwordTextBox").send_keys("1")
  time.sleep(1)
  driver.find_element(By.ID, "lp2-login-btn").click()
  time.sleep(5)
  assert True
  logout = "https://localhost:3005/app/logout"
  driver.get(logout)
  time.sleep(6)

  class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        driver.get("https://localhost:3005/app/test")
        # wait = WebDriverWait(driver, 5)
        # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))
        time.sleep(6)
# if __name__ == '__main__':
    unittest.main()
    time.sleep(6)
# Opens a new tab and switches to new tab
# driver.switch_to.new_window('tab')
# driver.close()
# driver.back()
# driver.navigate().forward()
# search_bar = driver.find_element_by_name("q")
# search_bar.clear()
# search_bar.send_keys("getting started with python")
# search_bar.send_keys(Keys.RETURN)
  
#   proxy.har # returns a HAR JSON blob
#   server.stop()

# driver.close()
finally:
    # driver.minimize_window()
    # driver.fullscreen_window()
    driver.quit()
