import pytest
import re


def ucbucaq_cevre(a, b, c):
    return a+b+c


def ucbucaq_alan(asagi, yuxari):
    return (asagi * yuxari) / 2


@pytest.fixture()
def hesabla():
    print("Hesablamalar basladi...")
    yield
    print("Hesablamalar bitdi.")


def test_ucbucaq_cevresi(hesabla):
    assert ucbucaq_cevre(3, 4, 4) == 11


def test_ucbucaq_alani(hesabla):
    assert ucbucaq_alan(5, 4) == 10
