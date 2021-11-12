link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_users_should_see_add_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")