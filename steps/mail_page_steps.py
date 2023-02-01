from selenium.webdriver import Keys
import steps.common_page_steps as cps
from pages.mail_page import MailPage


def send_letter(driver):
    refresh_by_click_on_link(driver)
    cps.find_element_by_xpath(driver, MailPage.create_letter_button, 5).click()
    fill_letter(driver)
    cps.find_element_by_xpath(driver, MailPage.send_letter_button, 1).click()


def refresh_by_click_on_link(driver):
    cps.find_element_by_xpath(driver, MailPage.email_link_in_header, 5).click()


def fill_letter(driver):
    cps.find_element_by_xpath(driver, MailPage.email_field, 3).send_keys(MailPage.SECOND_EMAIL)
    subject_field = cps.find_element_by_xpath(driver, MailPage.subject_field, 0.1)
    subject_field.send_keys(MailPage.LETTER_SUBJECT + Keys.TAB + Keys.TAB + MailPage.LETTER_TEXT)


def exit_from_account(driver):
    cps.find_element_by_xpath(driver, MailPage.right_menu_button, 1).click()
    cps.find_element_by_xpath(driver, MailPage.exit_button, 1).click()


def check_that_letter_delivered(driver):
    # wait until 70 second as mail.ru may have a delay in receiving
    cps.find_element_by_xpath(driver, MailPage.received_letter, 70).click()
    sender = cps.find_element_by_xpath(driver, MailPage.letter_sender, 3).get_attribute("title")
    received_letter_subject = cps.find_element_by_xpath(driver, MailPage.received_letter_subject, 0.1).text

    return sender, received_letter_subject
