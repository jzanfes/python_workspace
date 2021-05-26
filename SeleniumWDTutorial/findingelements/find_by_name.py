from selenium import webdriver

class FindByIdName:

    def test(self, base_url=None, el_id=None, el_name=None):
        if base_url == None:
            exit(code="No Url Specified")
        driver = webdriver.Chrome()
        try:
            driver.get(base_url)
        except:
            print("Url invalid or incorrectly entered!")
        if el_id is not None:
            try:
                i = driver.find_element_by_id(el_id)
                if i is not None:
                    print("An element was found by Id")
            except:
                    print("An error occurred check search value for Id")
        if el_name is not None:
            try:
                x = driver.find_element_by_name(el_name)
                if x is not None:
                    print("An element was found by Name")
            except:
                print("An error occurred check search value for Name")


x = FindByIdName()
x.test()

