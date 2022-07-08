import time

from selenium import webdriver

class ChromeDriverMac():

    def test(self):
        #instantiate chromer browser command
        driver = webdriver.Chrome(executable_path="/home/mrawal/Downloads/chromedriver")
        #open provided url
        driver.get("https://www.google.com")
        time.sleep(20)

cc = ChromeDriverMac()
cc.test()