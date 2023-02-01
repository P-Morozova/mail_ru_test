from pages.common_page import CommonPage


class LoginPage(CommonPage):
    FIRST_LOGIN = "test.firstman"
    FIRST_PASSWORD = "t2n1xAxaVRP"

    SECOND_LOGIN = "test.secondman"
    SECOND_PASSWORD = "YOiURrjps71"

    login_iframe = "//div[@class='ag-popup__frame__layout ag-popup__frame__layout-desktop']/iframe"

    login_field = "//input[@name='username']"
    password_field = "//input[@name='password']"
    next_button = "//div[@class='submit-button-wrap']//button"
