from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators 
from utils.generate_data import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data import click_element, fill_field, is_element_present 


class TestLogout:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"
    
    def test_successful_logout(self, driver):
        #Тест 5: Успешный выход пользователя
        # 1. Авторизация
        driver.get(self.BASE_URL)
        click_element(driver, Locators.LOGIN_REGISTRATION_BUTTON)
        fill_field(driver, Locators.EMAIL_INPUT, TEST_USER_EMAIL)
        fill_field(driver, Locators.PASSWORD_INPUT, TEST_USER_PASSWORD)
        click_element(driver, Locators.LOGIN_BUTTON)
        
        # 2. Дождаться завершения авторизации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.USER_AVATAR) 
        )
        
        # 3. Проверить, что пользователь авторизован
        assert is_element_present(driver, Locators.USER_AVATAR), \
            "Пользователь не авторизовался"
        
        # 4. Нажать кнопку «Выйти»
        click_element(driver, Locators.LOGOUT_BUTTON)
        
        # 5. Проверка: аватар и имя больше не отображаются
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(Locators.USER_AVATAR)
        )
        
        assert not is_element_present(driver, Locators.USER_AVATAR, timeout=3), \
            "Аватар пользователя всё ещё отображается после выхода"
        assert not is_element_present(driver, Locators.USER_NAME, timeout=3), \
            "Имя пользователя всё ещё отображается после выхода"
        
        # 6. Проверка: отображается кнопка «Вход и регистрация»
        assert is_element_present(driver, Locators.LOGIN_REGISTRATION_BUTTON), \
            "Кнопка 'Вход и регистрация' не отображается после выхода"
        
        print("✅ Тест пройден: пользователь успешно вышел из системы")

