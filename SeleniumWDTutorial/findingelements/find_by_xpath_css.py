from selenium import webdriver


class FindByXpathCss:

    def test(self, base_url=None, el_xpath=None, el_css=None):
        if base_url == None:
            exit(code="No Url Specified")
        driver = webdriver.Chrome()
        try:
            driver.get(base_url)
        except:
            exit(code="Url invalid or incorrectly entered!")
        if el_xpath is not None:
            try:
                i = driver.find_element_by_xpath(el_xpath)
                if i is not None:
                    print("An element was found by Xpath")
            except:
                print("An error occured check search value for Xpath")
        if el_css is not None:
            try:
                g = driver.find_element_by_css_selector(el_css)
                if g is not None:
                    print("An element was found by Css Selector")
            except:
                print("An error occurred check search value for Css Selector")


x = FindByXpathCss()
x.test("https://www.yahoo.com/", "//a[contains(text(),'Finance')]", "#ybar-navigation > div > ul > li:nth-child(4) > a")