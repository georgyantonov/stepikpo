from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def cart_is_empty(self):
        assert len(self.browser.find_elements(*BasketPageLocators.CHECK_CART)) == 0, 'Корзина не пуста'

    def cart_text_that_cart_is_empty(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.CHECK_TEXT_THAT_CART_IS_EMPTY).text