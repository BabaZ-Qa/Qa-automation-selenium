import unittest
import pytest
from Tests_Pages.aramasayfasi import AramaSehifesi
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("test_setup")
@ddt
class TestAramaSehifesi(unittest.TestCase):
    @data(("abc", "No products were found that matched your criteria."))
    @unpack
    def test_aramaya_iki_harfli_cikan_hatayi_dogrula(self, kelime, beklenen_mesaj):
        arama_butonu = AramaSehifesi(self.driver)
        arama_butonu.arama_butonunu_bul_yaz_tikla(kelime)

        message = arama_butonu.arama_butonuna_iki_harf_yazanda_mesaji_dogrula()
        assert message == beklenen_mesaj
