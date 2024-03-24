

class DzenPage(BasePage):

    def click_to_element(self, locator):
        self.find_element_with_wait(locator)