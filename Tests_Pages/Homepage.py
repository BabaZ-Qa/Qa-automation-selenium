from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Tests_Pages.PageBase import PageBase
from Tests_Pages.Laptop_cart_page import LaptopCartpage


class Homepage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LAPTOP_URUNU = ((
        By.XPATH, "//h2/a[text()='14.1-inch Laptop']"))
    SEHIFENIN_YUKARISINDAKI_URUNLERI_DOGRULA = (
        By.XPATH, "//ul[@class='top-menu']/li/a")
    ARAMA_KUTUSU = (By.ID, "small-searchterms")
    DIAMOND_URUNLER = (By.XPATH, "//div[@class='product-item']//h2/a")
    DIGITAL_DOWNLOADS = (By.XPATH, "//a[contains(text(),'Digital downloads')]")
    DIGITAL_DOWNLOADS_URUNLERI = (By.CSS_SELECTOR, "div h2 a")
    APPAREL_SHOES = (By.XPATH, "//li/a[contains(text(),'Apparel & Shoes')]")
    APPAREL_SHOES_URUNLER = (By.CSS_SELECTOR, "h2.product-title a")

    BOOKS_LINKI = (
        By.XPATH, "//li[@class='inactive']/a[contains(text(),'Books')]")

    def laptop_urunune_tikla(self):
        self.driver.find_element(*Homepage.LAPTOP_URUNU).click()
        laptop_page = LaptopCartpage(self.driver)
        return laptop_page

    def sehifedeki_yukari_kisimdaki_nesneleri_dogrulamak(self):
        dogru = [
            item.text for item in self.driver.find_elements(*Homepage.SEHIFENIN_YUKARISINDAKI_URUNLERI_DOGRULA)]
        return dogru

    def books_linkine_tikla(self):
        self.driver.find_element(*Homepage.BOOKS_LINKI).click()
        books_urununu_secme = LaptopCartpage(self.driver)
        return books_urununu_secme

    def ust_taraftaki_books_kismina_tikla(self):
        self.driver.find_element(
            By.XPATH, "//li/a[contains(text(),'Books')]").click()
        urunun_sayfasi = LaptopCartpage(self.driver)
        return urunun_sayfasi

    def arama_kutusunu_bul_ve_yazz(self, aranan):
        self.wait_element_presence(Homepage.ARAMA_KUTUSU)
        arama = self.driver.find_element(
            *Homepage.ARAMA_KUTUSU)
        arama.send_keys(aranan)
        arama.send_keys(Keys.ENTER)
        self.wait_element_visibility(Homepage.DIAMOND_URUNLER)

    def aranan_urunun_dogru_ciktigini_dogrula(self):
        aranan_urunler = [item.text for item in self.driver.find_elements(
            *Homepage.DIAMOND_URUNLER)]
        return aranan_urunler

    def digital_downloads_tikla(self):
        self.driver.find_element(*Homepage.DIGITAL_DOWNLOADS).click()
        self.wait_element_visibility(Homepage.DIGITAL_DOWNLOADS_URUNLERI)

    def cikan_digital_aramalarini_dogrula(self):
        ua = [urun.text for urun in self.driver.find_elements(
            *Homepage.DIGITAL_DOWNLOADS_URUNLERI)]
        return ua

    def apparel_shoes_tikla(self):
        self.driver.find_element(*Homepage.APPAREL_SHOES).click()
        self.wait_element_visibility(Homepage.APPAREL_SHOES_URUNLER)

    def apparel_shoes_urunlerini_dogrula(self):
        aurun = [urun.text for urun in self.driver.find_elements(
            *Homepage.APPAREL_SHOES_URUNLER)]
        return aurun
