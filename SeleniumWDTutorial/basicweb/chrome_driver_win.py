from selenium import webdriver


class ChromeDriverWin:

    def test_method(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ferrari.com")


chrm = ChromeDriverWin()
chrm.test_method()