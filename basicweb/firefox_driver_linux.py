import time

from selenium import webdriver

class RunFFTests():
    def testMethod(self):
        # instantiate ff browser command
        # driver = webdriver.Firefox(executable_path="/home/mrawal/Downloads/geckodriver")
        driver = webdriver.Chrome()
        # open provided url
        driver.get("https://www.letskodeit.com")
        time.sleep(20)

ff = RunFFTests()
ff.testMethod()