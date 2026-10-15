from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

from identity.loginLocator.loginLocatorPage import LoginActionLocator

# url = "https://www.saucedemo.com/"

class LoginActionPage:

    def __init__(self, driver):
        self.driver = driver

    def open_login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(LoginActionLocator.USERNAME)
        )
        element.send_keys(username)

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(LoginActionLocator.PASSWORD)
        )
        element.send_keys(password)

    def login(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(LoginActionLocator.LOGIN)
        )
        element.click()


