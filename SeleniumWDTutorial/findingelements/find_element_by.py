from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementBy:

    def test(self, base_url=None, el_by_id=None, el_by_xpath=None, el_by_linktext=None):
        if base_url == None:
            exit(code="No Url Specified")
        driver = webdriver.Chrome()
        try:
            driver.get(base_url)
        except:
            exit(code="Url invalid or incorrectly entered!")
        if el_by_id is not None:
            try:
                i = driver.find_element(By.ID, el_by_id)
                if i is not None:
                    print("An element was found by ID")
            except :
                print("An error occurred, check search value for ID")
        if el_by_xpath is not None:
            try:
                i = driver.find_element(By.XPATH, el_by_xpath)
                if i is not None:
                    print("An element was found by Xpath")
            except:
                print("An error occurred, check search value for Xpath")
        if el_by_linktext is not None:
            try:
                i = driver.find_element(By.LINK_TEXT, el_by_linktext)
                if i is not None:
                    print("An element was found by Link Text")
            except:
                print("An error occurred, check search value for Link Text")

chrm = FindElementBy()
chrm.test()