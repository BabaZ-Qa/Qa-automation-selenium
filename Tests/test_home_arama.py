import pytest
from Tests_Pages.Homepage import Homepage
from ddt import ddt, data, unpack
import unittest


@pytest.mark.usefixtures("test_setup")
@ddt
class TestArananUrun(unittest.TestCase):
    urunler = ["Black & White Diamond Heart", "Diamond Pave Earrings",
               "Diamond Tennis Bracelet", "Vintage Style Three Stone Diamond Engagement Ring"]

    @data(("diamond", urunler))
    @unpack
    def test_urunleri_bul_ve_dogrula(self, urun, expected_result):
        anasehife = Homepage(self.driver)
        anasehife.arama_kutusunu_bul_ve_yazz(urun)
        actual_result = anasehife.aranan_urunun_dogru_ciktigini_dogrula()
        assert expected_result == actual_result
