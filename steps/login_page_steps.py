from pages.login_page import LoginPage
import steps.common_page_steps as cps

def login_on_mail(driver, login, password):
    cps.click_on_login_button(driver)
    driver.switch_to.frame(cps.find_element_by_xpath(driver, LoginPage.login_iframe, 3))
    cps.find_element_by_xpath(driver, LoginPage.login_field, 3).send_keys(login)
    cps.find_element_by_xpath(driver, LoginPage.next_button, 3).click()
    cps.find_element_by_xpath(driver, LoginPage.password_field, 3).send_keys(password)
    cps.find_element_by_xpath(driver, LoginPage.next_button, 3).click()