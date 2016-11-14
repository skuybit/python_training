# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver


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
    wd.find_element_by_css_selector("a.team.yankees").click()
    wd.back()
    wd.find_element_by_css_selector("a.team.mets").click()
    wd.back()
    wd.find_element_by_css_selector("a.team.giants").click()
    wd.back()
    wd.find_element_by_css_selector("a.team.jets").click()
    wd.back()
    wd.find_element_by_css_selector("a.team.knicks").click()
    wd.back()
    wd.find_element_by_css_selector("a.team.nets").click()
    wd.back()
    wd.find_element_by_css_selector("a.team.rangers").click()
    wd.back()
    wd.find_element_by_css_selector("a.team.islanders").click()
    wd.back()
    wd.find_element_by_xpath("//main[@id='r-main']//a[.='More Sports']").click()
    wd.back()


finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
