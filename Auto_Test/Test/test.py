from selenium import webdriver
import unittest
import time
from Page.Start import Start
from Page.Cart import Cart


class Rivegauche_ru(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://rivegauche.ru/')

    def test_Search(self):
        riv = Start(self.driver)
        time.sleep(2)
        riv.search()
        time.sleep(2)
        riv.chanel()
        time.sleep(2)
        assert 'COCO MADEMOISELLE' in self.driver.page_source
        pass

    def test_Location(self):
        riv = Start(self.driver)
        time.sleep(2)
        riv.location()
        time.sleep(2)
        riv.aban()
        time.sleep(2)
        assert 'Абан' in self.driver.page_source
        pass

    def test_Reg(self):
        riv = Start(self.driver)
        time.sleep(2)
        riv.user()
        time.sleep(2)
        riv.reg()
        time.sleep(2)
        assert 'Регистрация' in self.driver.page_source
        pass

    def test_Cart(self):
        riv = Start(self.driver)
        time.sleep(2)
        riv.search()
        time.sleep(2)
        riv.chanel()
        time.sleep(2)
        riv.coco()
        time.sleep(2)
        riv.add_to_cart()
        time.sleep(3)
        riv.cart()
        time.sleep(2)
        assert 'ПАРФЮМИРОВАННАЯ ВОДА СПРЕЙ' in self.driver.page_source
        pass

    def test_Delete(self):
        riv = Start(self.driver)
        cart = Cart(self.driver)
        time.sleep(2)
        riv.search()
        time.sleep(2)
        riv.chanel()
        time.sleep(2)
        riv.coco()
        time.sleep(2)
        riv.add_to_cart()
        time.sleep(2)
        riv.cart()
        time.sleep(2)
        cart.delete()
        time.sleep(2)
        assert 'Ваша корзина пуста' in self.driver.page_source
        pass

    def Quit(self):
        self.driver.close()
        self.driver.quit()
