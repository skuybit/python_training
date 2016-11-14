# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://www.nydailynews.com/")
    wd.find_element_by_id("rh").click()
    wd.find_element_by_link_text("DONALD TRUMP TRANSITION").click()
    wd.back()
    wd.find_element_by_link_text("HILLARY CLINTON").click()
    wd.back()
    wd.find_element_by_link_text("BARACK OBAMA").click()
    wd.back()
    wd.find_element_by_link_text("ROB KARDASHIAN").click()
    wd.find_element_by_link_text("ROB KARDASHIAN").click()
    wd.back()
    wd.find_element_by_link_text("BARTOLO COLON").click()
    wd.back()
    wd.find_element_by_link_text("New York Daily News").click()
    wd.find_element_by_link_text("New York Daily News").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
