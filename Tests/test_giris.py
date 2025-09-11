import pytest


def toplama(a, b):
    return a + b


def cixma(a, b):
    return a - b


def vurma(a, b):
    return a * b


def bolme(a, b):
    return a / b


@pytest.fixture()
def hesablama():
    print("Hesablamalar edildi")


def test_toplama(hesablama):
    assert toplama(2, 2) == 4


def test_cixma(hesablama):
    assert cixma(5, 3) == 2


def test_vurma(hesablama):
    assert vurma(2, 3) == 6


def test_bolme(hesablama):
    assert bolme(6, 2) == 3
