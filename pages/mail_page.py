from pages.common_page import CommonPage


class MailPage(CommonPage):
    LETTER_SUBJECT = "Test Subject"
    LETTER_TEXT = "Dear TestMan, How are You?"

    create_letter_button = "//a[@href='/compose/']"
    email_field = "//div[starts-with(@class, 'inputContainer')]/input[1]"
    subject_field = "//input[@name='Subject']"
    send_letter_button = "//span[contains(text(),'Отправить')]"

    right_menu_button = "//div[@id='ph-whiteline']//span[2]"
    exit_button = "//div[contains(text(),'Выйти')]"

    received_letter = "//div[@class='ReactVirtualized__Grid__innerScrollContainer']/a[1]"
    letter_sender = "//span[@class='letter-contact']"
    received_letter_subject = "//h2[@class='thread-subject']"


