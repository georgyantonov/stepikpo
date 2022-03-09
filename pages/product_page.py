from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_cart(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_basket_button.click()

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Cart button is not presented"

    def should_be_page_item_url(self):
        assert '?promo=offer' in self.browser.current_url, "Ссылка на страницу товара неверная"

    def should_be_correct_text_after_add_item_to_cart(self):
        text_of_answer = self.browser.find_element(*ProductPageLocators.CHECK_TEXT_AFTER_ADD_CART).text
        assert text_of_answer == 'Coders at Work', 'Текст после добавления товара в ' \
                                                                                  'корзину неверный '

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_dissapeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not dissapeared, but should be"