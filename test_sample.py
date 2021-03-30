import pytest
from selenium import webdriver


def test_sample():
    driver = webdriver.Chrome()
    driver.get('https://demo.opencart.com/')
    assert driver.current_url == 'https://demo.opencart.com/'
