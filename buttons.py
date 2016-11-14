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
    wd.find_element_by_link_text("Facebook").click()
    wd.back()
    wd.find_element_by_link_text("Twitter").click()
    wd.back()
    wd.find_element_by_link_text("Instagram").click()
    wd.back()
    wd.find_element_by_id("rh-follow-btn").click()
    wd.find_element_by_css_selector("span.ri-close").click()
    wd.find_element_by_id("rh-subscribe").click()
    wd.find_element_by_xpath("//div[@id='rho-subscribe-desk']//span[.='Subscribe']").click()
    wd.find_element_by_id("rh-sections").click()
    wd.find_element_by_id("rho-sections-close").click()


finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
