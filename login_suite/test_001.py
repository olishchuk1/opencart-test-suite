import pytest
from selenium import webdriver
from time import sleep


def test_001():
    driver = webdriver.Chrome()
    driver.get('https://demo.opencart.com/')
    driver.maximize_window()
    driver.find_element_by_link_text('My Account').click()
    driver.find_element_by_link_text('Login').click()

    