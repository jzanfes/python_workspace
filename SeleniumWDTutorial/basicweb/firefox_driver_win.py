from selenium import webdriver


class FireFoxDriverWin:

    def test_method(self):
        driver = webdriver.Firefox()
        driver.get("https://www.ferrari.com")


fox = FireFoxDriverWin()
fox.test_method()