import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from utils.test_data import find_element, click_element, fill_field, get_text
from utils.generate_data import generate_email, generate_ad_description, generate_ad_title, generate_price, TEST_USER_EMAIL, TEST_USER_PASSWORD, AUTH_MODAL_TITLE_TEXT
from utils.urls import BASE_URL


class TestCreateAdvertisement:
    
    def test_create_ad_unauthorized(self, driver):
        #Тест 6: Создание объявления неавторизованным пользователем
        # 1. Открыть главную страницу
        driver.get(BASE_URL)
        
        # 2. Нажать кнопку «Разместить объявление»
        click_element(driver, Locators.CREATE_AD_BUTTON)
        
        # 3. Проверка: отображается модальное окно
        modal_title = get_text(driver, Locators.AUTH_MODAL_TITLE)
        
        assert modal_title == AUTH_MODAL_TITLE_TEXT, \
            f"Неверный заголовок модального окна. Ожидалось: 'Чтобы разместить объявление, авторизуйтесь', Получено: '{modal_title}'"
        
        print("✅ Тест пройден: неавторизованный пользователь не может создать объявление")
    
    def test_create_ad_authorized(self, driver):
        #Тест 7: Создание объявления авторизованным пользователем
        # 1. Авторизация
        driver.get(BASE_URL)
        click_element(driver, Locators.LOGIN_REGISTRATION_BUTTON)
        fill_field(driver, Locators.EMAIL_INPUT, TEST_USER_EMAIL)
        fill_field(driver, Locators.PASSWORD_INPUT, TEST_USER_PASSWORD)
        click_element(driver, Locators.LOGIN_BUTTON)
        
        # 2. Дождаться завершения авторизации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.USER_AVATAR) 
        )
        
        # 3. Перейти в профиль пользователя
        click_element(driver, Locators.USER_AVATAR)

        # 4. Получить количество существующих объявлений 
        old_ad_count = len(driver.find_elements(*Locators.LAST_AD_CARD))
        print(f"📊 Было объявлений до теста: {old_ad_count}")

        # 5. Нажать "Разместить объявление"
        click_element(driver, Locators.CREATE_AD_BUTTON)
        
        # 6. Заполнить все поля формы
        title = generate_ad_title()
        description = generate_ad_description()
        price = generate_price()
        
        fill_field(driver, Locators.AD_TITLE_INPUT, title)
        fill_field(driver, Locators.AD_DESCRIPTION_INPUT, description)
        fill_field(driver, Locators.AD_PRICE_INPUT, str(price))
        
        # 7. Выбрать категорию 
        # Клик по стрелке 
        click_element(driver, Locators.CATEGORY_ARROW_BUTTON)
    
        # Выбор категории "Книги"
        category_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.CATEGORY_DROPDOWN_SELECTION)
        )
        category_option.click()
    
        # 8. Выбрать город 
        # Клик по стрелке 
        click_element(driver, Locators.CITY_ARROW_BUTTON)
    
        # Выбор города "Санкт-Петербург"
        city_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.CITY_DROPDOWN_SELECTION)
        )
        city_option.click()
    
        # 9. Выбрать состояние товара «Б/у»
        click_element(driver, Locators.USED_CONDITION_RADIO)
    
        # 10. Нажать кнопку «Опубликовать»
        click_element(driver, Locators.PUBLISH_BUTTON)
    
        # 11. Дождаться сохранения
        time.sleep(5)  

        driver.refresh()
    
        # 12. Перейти в профиль пользователя
        click_element(driver, Locators.USER_AVATAR)

        driver.refresh()
    
        # 13. Проверка: в блоке «Мои объявления» отображается созданное объявление
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.LAST_AD_CARD)
        )
    
        # Получить количество объявлений после создания
        new_ad_count = len(driver.find_elements(*Locators.LAST_AD_CARD))
        print(f"📊 Стало объявлений после теста: {new_ad_count}")

        # Проверяем, что количество объявлений увеличилось на 1
        assert new_ad_count == old_ad_count + 1, \
            f"Количество объявлений не увеличилось. Было: {old_ad_count}, Стало: {new_ad_count}"
    
        print(f"✅ Тест пройден: объявление успешно создано")
    
