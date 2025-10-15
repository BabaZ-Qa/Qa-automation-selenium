import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Tests_Pages.PageBase import PageBase


class AramaSehifesi(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ARAMA_KUTUSU = (By.ID, "small-searchterms")
    ARAMADAN_SONRAKI_MESAJ = (By.XPATH, "//strong[@class='result']")

    def arama_butonunu_bul_yaz_tikla(self, kelime):
        button = self.driver.find_element(*AramaSehifesi.ARAMA_KUTUSU)
        button.send_keys(kelime)
        button.send_keys(Keys.ENTER)
        self.wait_element_visibility(AramaSehifesi.ARAMADAN_SONRAKI_MESAJ)

    def arama_butonuna_iki_harf_yazanda_mesaji_dogrula(self):
        mesaj = self.driver.find_element(
            *AramaSehifesi.ARAMADAN_SONRAKI_MESAJ).text
        return mesaj
