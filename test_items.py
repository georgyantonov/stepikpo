from selenium.webdriver.common.by import By
def test_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_btn = browser.find_element(By.CLASS_NAME,"btn-add-to-basket")
    assert add_btn, f'Кнопка добавления в корзину присутствует'