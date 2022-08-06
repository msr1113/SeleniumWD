from selenium import webdriver

class BrowserInteraction():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver= webdriver.Firefox()

        driver.maximize_window()

        driver.get(baseUrl)

        title = driver.title
        print('title of webpage is:'+title)

        currentUrl = driver.current_url
        print('current url of page is'+currentUrl)

        driver.refresh()
        print("browser refreshed 1st time")
        driver.get(driver.current_url)
        print("browser refreshed 2nd time")

        driver.get("https://courses.letskodeit.com/login")
        currentUrl=driver.current_url
        print('current url of page is' + currentUrl)
        driver.back()
        currentUrl = driver.current_url
        print('current url of page is' + currentUrl)
        print("go one step back in browser history")
        driver.forward()
        currentUrl = driver.current_url
        print('current url of page is' + currentUrl)
        print("go one step forward in browser history")

        pageSource = driver.page_source
        print(pageSource)
        # driver.close()
        driver.quit()

ff = BrowserInteraction()
ff.test()



