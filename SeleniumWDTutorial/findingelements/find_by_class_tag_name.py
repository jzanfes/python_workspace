from selenium import webdriver

class FindByIdClassTagName:

    def test(self, base_url=None, class_name=None, tag_name=None):
        if base_url == None:
            exit(code="No Url Specified")
        driver = webdriver.Chrome()
        try:
            driver.get(base_url)
        except:
            print("Url invalid or incorrectly entered!")
        if class_name is not None:
            try:
                i = driver.find_element_by_class_name(class_name)
                if i is not None:
                    print("An element was found by Class Name")
            except :
                print("An error occurred, check search value for Class Name")
        if tag_name is not None:
            try:
                x = driver.find_element_by_tag_name(tag_name)
                if x is not None:
                    print("An element was found by Tag Name")
            except:
                print("An error occurred check search value for Tag Name")


chrm = FindByIdClassTagName()
chrm.test("https://www.yahoo.com/", "")