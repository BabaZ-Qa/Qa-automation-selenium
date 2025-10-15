import requests


def test_get_post():
    response = requests.get(
        "https://demowebshop.tricentis.com/computing-and-internet")
    assert response.status_code == 200
