import time
import steps.mail_page_steps as mps
import steps.common_page_steps as cps
import steps.login_page_steps as lps
from pages.login_page import LoginPage
from pages.mail_page import MailPage


def test_mail_ru(driver):

    cps.get_link(driver)
    lps.login_on_mail(driver, LoginPage.FIRST_LOGIN, LoginPage.FIRST_PASSWORD)
    mps.send_letter(driver)
    mps.exit_from_account(driver)

    lps.login_on_mail(driver, LoginPage.SECOND_LOGIN, LoginPage.SECOND_PASSWORD)

    sender_email, sender_theme = mps.check_that_letter_delivered(driver)

    assert sender_email == LoginPage.FIRST_EMAIL, \
        "The sender of the received message does not match the sender of the sent message!"
    assert sender_theme == MailPage.LETTER_SUBJECT, \
        "The subject of the received email does not match the subject of the sent one!"
