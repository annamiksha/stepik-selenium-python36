from datetime import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_buy_button(browser):
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    time.sleep(30)
    assert button.text is not None, 'Текст кнопки не обнаружен'
