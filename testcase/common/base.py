# -*- coding: utf-8 -*-
from .driver import Driver
import os
import time
from selenium.webdriver.support.ui import WebDriverWait


class BaseUse(object):
    def __init__(self):
        self.dr = Driver()
        self.dr.connect()
        self.driver = self.dr.get_driver()

    def find_element(self, *loc):
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))
        return element

