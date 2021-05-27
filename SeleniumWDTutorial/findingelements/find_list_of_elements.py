from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements:

    def test(self, base_url=None, els_by_class_name=None, els_by_tag_name=None):
        if base_url == None:
            exit(code="No Url Specified")
        driver = webdriver.Chrome()
        try:
            driver.get(base_url)
        except:
            exit(code="Url invalid or incorrectly entered!")
        if els_by_class_name is not None:
            try:
                cn = len(driver.find_elements(By.CLASS_NAME, els_by_class_name))
                if cn is not None:
                    print(f"{cn} class-name='{els_by_class_name}' instances found!")
            except :
                print("An error occurred, check search value for ID")
        if els_by_tag_name is not None:
            try:
                tn = len(driver.find_elements(By.TAG_NAME, els_by_tag_name))
                if tn is not None:
                    print(f"{tn} tag-name='{els_by_tag_name}' instances found!")
            except:
                print("An error occurred, check search value for Xpath")


chrm = ListOfElements()
chrm.test("https://www.usd.edu/", "fb_reset", "div")