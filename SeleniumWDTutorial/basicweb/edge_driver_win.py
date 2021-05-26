from selenium import webdriver


class EdgeDriverWin:

    def test_method(self):
        driver = webdriver.Edge()
        driver.get("https://www.ferrari.com")


edg = EdgeDriverWin()
edg.test_method()