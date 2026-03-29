from selenium.webdriver.support import expected_conditions as EC
from locators import Locators 
from utils.generate_data import TEST_USER_EMAIL, TEST_USER_PASSWORD
from utils.test_data import click_element, fill_field, is_element_present 


class TestLogin:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"
    
    def test_successful_login(self, driver):
        #Тест 4: Успешный вход пользователя
        # 1. Открыть главную страницу
        driver.get(self.BASE_URL)
        
        # 2. Нажать кнопку «Вход и регистрация»
        click_element(driver, Locators.LOGIN_REGISTRATION_BUTTON)
        
        # 3. Заполнить все поля формы авторизации
        fill_field(driver, Locators.EMAIL_INPUT, TEST_USER_EMAIL)
        fill_field(driver, Locators.PASSWORD_INPUT, TEST_USER_PASSWORD)
        
        # 4. Нажать кнопку «Войти»
        click_element(driver, Locators.LOGIN_BUTTON)
        
        # 5. Проверка: переход на главную страницу
        current_url = driver.current_url
        expected_url = self.BASE_URL
    
        assert current_url == expected_url, \
            f"   Ожидаемый URL: {expected_url}\n" \
            f"   Фактический URL: {current_url}\n" \
        
        # 6. Проверка: отображается аватар пользователя
        assert is_element_present(driver, Locators.USER_AVATAR), \
            "Аватар пользователя не отображается после входа"
        
        # 7. Проверка: отображается имя User
        assert is_element_present(driver, Locators.USER_NAME), \
            "Имя пользователя не отображается после входа"
        
        print(f"✅ Тест пройден: пользователь {TEST_USER_EMAIL} успешно вошел в систему")