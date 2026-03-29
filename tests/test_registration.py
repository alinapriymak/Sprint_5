from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from utils.test_data import find_element, click_element, fill_field, is_element_present
from utils.generate_data import generate_email, generate_password, TEST_USER_EMAIL, TEST_USER_PASSWORD


class TestRegistration:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"
    
    def test_successful_registration(self, driver):
        #Тест 1: Успешная регистрация пользователя
        # 1. Открыть главную страницу
        driver.get(self.BASE_URL)
        
        # 2. Нажать кнопку «Вход и регистрация»
        click_element(driver, Locators.LOGIN_REGISTRATION_BUTTON)
        
        # 3. Нажать кнопку «Нет аккаунта»
        click_element(driver, Locators.NO_ACCOUNT_BUTTON)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
        )
    
        # 4. Заполнить все поля формы регистрации
        email = generate_email()
        password = generate_password()
        
        fill_field(driver, Locators.EMAIL_INPUT, email)
        fill_field(driver, Locators.PASSWORD_INPUT, password)
        fill_field(driver, Locators.SUBMIT_PASSWORD_INPUT, password)
        
        # 5. Нажать кнопку «Создать аккаунт»
        click_element(driver, Locators.CREATE_ACCOUNT_BUTTON)

        
        # 6. Проверка: переход на главную страницу
        current_url = driver.current_url
        expected_url = self.BASE_URL
    
        assert current_url == expected_url, \
            f"   Ожидаемый URL: {expected_url}\n" \
            f"   Фактический URL: {current_url}\n" \
        
        
        # 7. Проверка: отображается аватар пользователя
        assert is_element_present(driver, Locators.USER_AVATAR), \
        "Аватар пользователя не отображается после регистрации"
        
        # 8. Проверка: отображается имя User
        assert is_element_present(driver, Locators.USER_NAME)
        
        print(f"✅ Тест пройден: пользователь {email} успешно зарегистрирован")


    
    def test_registration_with_invalid_email(self, driver):
        #Тест 2: Регистрация с email не по маске
        # 1. Открыть главную страницу
        driver.get(self.BASE_URL)
        
        # 2. Нажать кнопку «Вход и регистрация»
        click_element(driver, Locators.LOGIN_REGISTRATION_BUTTON)
        
        # 3. Нажать кнопку «Нет аккаунта»
        click_element(driver, Locators.NO_ACCOUNT_BUTTON)
        
        # 4. Заполнить поле Email некорректным значением
        fill_field(driver, Locators.EMAIL_INPUT, "test.ru")
        
        # 5. Нажать кнопку «Создать аккаунт»
        click_element(driver, Locators.CREATE_ACCOUNT_BUTTON)
        
        # 6. Проверка: поля выделены красным
        error_fields = find_element(driver, Locators.ERROR_FIELDS, timeout=5)
        assert error_fields is not None, "Поля с ошибкой не выделены красным"
        
        # 7. Проверка: отображается сообщение «Ошибка»
        assert is_element_present(driver, Locators.EMAIL_ERROR), \
            "Сообщение об ошибке не отображается под полем Email"
        
        print("✅ Тест пройден: валидация некорректного email работает")
    

    def test_registration_existing_user(self, driver):
        #Тест 3: Регистрация уже существующего пользователя
        # 1. Открыть главную страницу
        driver.get(self.BASE_URL)
        
        # 2. Нажать кнопку «Вход и регистрация»
        click_element(driver, Locators.LOGIN_REGISTRATION_BUTTON)
        
        # 3. Нажать кнопку «Нет аккаунта»
        click_element(driver, Locators.NO_ACCOUNT_BUTTON)
        
        # 4. Заполнить поля данными существующего пользователя
        fill_field(driver, Locators.EMAIL_INPUT, TEST_USER_EMAIL)
        fill_field(driver, Locators.PASSWORD_INPUT, TEST_USER_PASSWORD)
        fill_field(driver, Locators.SUBMIT_PASSWORD_INPUT, TEST_USER_PASSWORD)
        
        # 5. Нажать кнопку «Создать аккаунт»
        click_element(driver, Locators.CREATE_ACCOUNT_BUTTON)
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ERROR_FIELDS)
        ) 
        
        # 7. Проверка: поля выделены красным
        error_fields = find_element(driver, Locators.ERROR_FIELDS, timeout=5)
        assert error_fields is not None, "Поля с ошибкой не выделены красным"
        
        # 8. Проверка: отображается сообщение «Ошибка»
        assert is_element_present(driver, Locators.EMAIL_ERROR), \
            "Сообщение об ошибке не отображается для существующего пользователя"
        
        print("✅ Тест пройден: попытка регистрации существующего пользователя отклонена")