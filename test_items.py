link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languege (browser):
    browser.get(link)
    fi = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    assert fi, "Кнопка не найдена"