from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Ссылка на страницу логина неверная"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "На странице регистрации и логина нет формы " \
                                                                         "логина "

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM), 'На странице регистрации и логина нет ' \
                                                                                'формы регистрации '

    def register_new_user(self, email, password):
        send_email = self.browser.find_element(*LoginPageLocators.ADD_EMAIL_FOR_REGISTRATION)
        send_email.send_keys(email)
        passwords = self.browser.find_elements(*LoginPageLocators.ADD_PASSWORD_FOR_REGISTRATION)
        for i in passwords:
            i.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()