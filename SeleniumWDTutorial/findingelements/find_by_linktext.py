from selenium import webdriver

class FindByLinkText:

    def test(self, base_url=None, link=None, partial_link=None):
        if base_url == None:
            exit(code="No Url Specified")
        driver = webdriver.Chrome()
        try:
            driver.get(base_url)
        except:
            exit(code="Url invalid or incorrectly entered!")
        if link is not None:
            try:
                i = driver.find_element_by_link_text(link)
                if i is not None:
                    print("An element was found by Link Text")
            except:
                print("An error occurred check search value for Link Text")
        if partial_link is not None:
            try:
                x = driver.find_element_by_partial_link_text(partial_link)
                if x is not None:
                    print("An element was found by Partial Link Text")
            except:
                print("An error occurred check search value for Partial Link Text")


x = FindByLinkText()
x.test("https://www.mathworks.com", partial_link="Deep Lea")