from selenium import webdriver

class RunFFTests():
    def testMethod(self):
        # instantiate ff browser command
        driver = webdriver.Firefox(executable_path="/home/mrawal/Downloads/geckodriver")
        # open provided url
        driver.get("https://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()