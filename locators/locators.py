from selenium.webdriver.common.by import By


class Locators:
    #Локаторы главной страницы
    LOGIN_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_AVATAR = (By.XPATH, "//button[@class='circleSmall']")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

    #Локаторы страницы авторизации/регистрации
    #Кнопки
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    #Инпуты
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_PASSWORD_INPUT = (By.XPATH, "//input[@name='submitPassword']")
    #Ошибки
    ERROR_FIELDS = (By.XPATH, "//div[contains(@class, 'input_inputError') and .//input[@name='password']]") 
    EMAIL_ERROR = (By.XPATH, "//div[contains(@class, 'input_inputError') and .//input[@name='email']]")

    #Локаторы страницы профиля
    #Инпуты
    AD_TITLE_INPUT = (By.XPATH, "//input[@name='name']")
    AD_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']") 
    AD_PRICE_INPUT = (By.XPATH, "//input[@name='price']") 
    #Дропдауны Город и Категория
    CATEGORY_ARROW_BUTTON = (By.XPATH, "//input[@name='category']/following-sibling::button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    CATEGORY_DROPDOWN_SELECTION = (By.XPATH, "//span[contains(text(), 'Книги')]")
    CITY_ARROW_BUTTON = (By.XPATH, "//input[@name='city']/following-sibling::button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    CITY_DROPDOWN_SELECTION = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]")
    #Радиокнопки "Состояние товара"
    USED_CONDITION_RADIO = (By.XPATH, "//input[@type='radio']/following-sibling::div[@class='radioUnput_inputRegular__FbVbr']")
    #Кнопка "Опубликовать"
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    #Карточка объявления
    LAST_AD_CARD = (By.XPATH, "//div[@class='card'][last()]")
    