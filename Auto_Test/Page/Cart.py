from selenium import webdriver
class Cart():
    def __init__(self, driver):
        self.driver = driver

        self.delete_button = '/html/body/app-root/layout/main/cart-page/div[1]/div/div[2]/a'

    def delete(self):
        self.driver.find_element_by_xpath(self.delete_button).click()


