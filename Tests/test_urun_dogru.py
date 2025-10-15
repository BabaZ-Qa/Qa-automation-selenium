import pytest
from Tests_Pages.Homepage import Homepage
from ddt import ddt, data, unpack
import unittest


@pytest.mark.usefixtures("test_setup")
@ddt
class TestUrunDogru(unittest.TestCase):
    urunler = ["3rd Album", "Music 2", "Music 2"]

    @data((urunler))
    def test_urunlerin_gorunurluyunu_dogrulama(self, beklenen_urunler):
        arama_sehifesi = Homepage(self.driver)
        arama_sehifesi.digital_downloads_tikla()
        mesaj = arama_sehifesi.cikan_digital_aramalarini_dogrula()
        assert mesaj == beklenen_urunler
