from selenium import webdriver

class FindIdName():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById=driver.find_element_by_id("name")

        if elementById is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("we found an element by name")

        driver.get("https://www.yahoo.com/")
        driver.find_element_by_class_name("_yb_1mve9")


ff = FindIdName()
ff.test()