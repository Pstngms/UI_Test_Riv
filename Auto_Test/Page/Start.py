from selenium import webdriver


class Start():
    def __init__(self, driver):
        self.driver = driver

        self.search_button = '/html/body/app-root/layout/header/div[2]/div[1]'
        self.chanel_button = '/html/body/overlay/div/site-search/div[2]/div[1]/ul/li[1]/a'
        self.location_button = '/html/body/app-root/layout/header/div[1]/cms-geo-locator'
        self.aban_button = '/html/body/overlay/div/region-selector/form/ng-scrollbar/div/div/div/div/ul/li[4]'
        self.user_button = '/html/body/app-root/layout/header/div[2]/div[2]'
        self.reg_button = '/html/body/overlay/div/auth-wnd/div/button'
        self.coco_button = '/html/body/app-root/layout/main/category-page/div/div[7]/div[2]/div/div[' \
                           '5]/product-carousel[2]/carousel/div[1]/div/div/carousel-item[1] '
        self.add_to_cart_button = '/html/body/app-root/layout/main/product-page/div[5]/div[2]/div[2]/div[3]/div[' \
                                  '2]/div/product-add-to-cart/button '
        self.cart_button = '/html/body/app-root/layout/header/div[2]/div[3]'

    def search(self):
        self.driver.find_element_by_xpath(self.search_button).click()

    def chanel(self):
        self.driver.find_element_by_xpath(self.chanel_button).click()

    def location(self):
        self.driver.find_element_by_xpath(self.location_button).click()

    def aban(self):
        self.driver.find_element_by_xpath(self.aban_button).click()

    def user(self):
        self.driver.find_element_by_xpath(self.user_button).click()

    def reg(self):
        self.driver.find_element_by_xpath(self.reg_button).click()

    def coco(self):
        self.driver.find_element_by_xpath(self.coco_button).click()

    def add_to_cart(self):
        self.driver.find_element_by_xpath(self.add_to_cart_button).click()

    def cart(self):
        self.driver.find_element_by_xpath(self.cart_button).click()

