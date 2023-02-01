from selenium.webdriver.support.wait import WebDriverWait
from pages.common_page import CommonPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_link(driver):
    return driver.get(CommonPage.LINK)


def find_element_by_xpath(driver, xpath, time):
    return WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH, xpath)),
                                             message=f"Can't find element by xpath: {xpath}")


def click_on_login_button(driver):
    find_element_by_xpath(driver, CommonPage.login_button, 3).click()


def click_on_email_link(driver):
    find_element_by_xpath(driver, CommonPage.email_link_in_header, 3).click()
