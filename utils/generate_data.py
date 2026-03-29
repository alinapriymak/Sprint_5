import random
import uuid



#Генерация имейла 
def generate_email():
    return f"test_{uuid.uuid4().hex[:10]}@test.com"


#Генерация пароля
def generate_password():
    return "TestPassword123"


#Генерация названия
def generate_ad_title():
    return f"Тестовое объявление {random.randint(1, 100)}"


#Генерация описания
def generate_ad_description():
    return f"Тестовое описание {random.randint(1, 100)}"


#Генерация цены
def generate_price():
    return random.randint(100, 10000)


# Тестовые учетные данные
TEST_USER_EMAIL = "test_user_for_tests@test.ru"
TEST_USER_PASSWORD = "pk4tA.D.en2DjZr"

AUTH_MODAL_TITLE_TEXT = "Чтобы разместить объявление, авторизуйтесь"