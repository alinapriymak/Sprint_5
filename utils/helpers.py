from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Найти элемент с ожиданием
def find_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


#Кликнуть по элементу
def click_element(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()


#Заполнить поле текстом
def fill_field(driver, locator, text, timeout=10):
    for attempt in range(3):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            return
        except Exception as e:
            if attempt == 2:
                raise e
            continue


#Проверить наличие элемента
def is_element_present(driver, locator, timeout=10):
    try:
        find_element(driver, locator, timeout)
        return True
    except:
        return False


#Получить текст элемента
def get_text(driver, locator, timeout=10):
    element = find_element(driver, locator, timeout)
    return element.text