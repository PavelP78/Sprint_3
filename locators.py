from selenium.webdriver.common.by import By

class StellarBurgersLocators:
    PASSWORD_FIELD = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input') # Поле пароль
    EMAIL_FIELD = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input') # Поле е-майл
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p') # Кнопка личный кабинет
    ENTER_BUTTON = (By.XPATH, '/html/body/div/div/main/div/form/button') # Кнопка войти
    MAIN_ENTER_BUTTON = (By.XPATH, '/html/body/div/div/main/section[2]/div/button') # Кнопка войти в аккаунт на главной
    ENTER_BUTTON_REGISTRATION_FORM = (By.XPATH, '/html/body/div/div/main/div/div/p/a') # Кнопка войти в аккаунт в форме регистрации
    BUTTON_PASSWORD_RECOVERY_FORM = (By.XPATH, '/html/body/div/div/main/div/div/p[2]/a') # Кнопка  восстановления пароля
    ENTER_BUTTON_PASSWORD_RECOVERY_FORM = (By.XPATH, '/html/body/div/div/main/div/div/p/a') # Кнопка войтив форме восстановления пароля
    REGISTRATION_BUTTON = (By.XPATH, '/html/body/div/div/main/div/div/p[1]/a') # Кнопка зарегистрироваться
    DESIGNER_BUTTON = (By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a/p') # Кнопка конструктор

    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']") # Логотип Stellar Burgers

    EXIT_BUTTON = (By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button') # Кнопка «Выйти» в личном кабинете
    ROLLS_BUTTON = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]/span') # Кнопка «Булки»
    SOUCE_BUTTON = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]/span') # Кнопка «Соусы»
    FILLING_BUTTON = (By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]/span') # Кнопка «Начинки»
    ENTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # Кнопка войти в аккаунт
    ERROR_PASSWORD= (By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/p') # Надпись некорректный пароль
    ORDER_BUTTON= (By.XPATH, '/html/body/div/div/main/section[2]/div/button') # Кнопка оформить заказ
    NAME_FIELD = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input') # Поле имя при регистрации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input') # Поле е-майл при регистрации
    PASSWORD_FIELD_REGISTRATION = (By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/div/input') # Поле пароль при регистрации
    REGISTRATION_BUTTON_REGISTRATION = (By.XPATH, '/html/body/div/div/main/div/form/button') # Кнопка зарегистрироваться на странице регистрации
    ERROR_PASSWORD_REGISTRATION= (By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/p') # Надпись некорректный пароль на странице регистрации
    ROLLS_PICTURE = (By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]/img') # Картинка флюоресцентная булка
    SOUCE_PICTURE = (By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[2]/a[1]/img') # Картинка соус Spisy-x
    FILLING_PICTURE = (By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[3]/a[2]/img') # Картинка начинки говяжий метеорит

    SAVE_BUTTON= (By.XPATH, '/html/body/div/div/main/div/div/div/div/button[2]') # Кнопка сохранить


    PERSONAL_ACCOUNT_BUTTON_2 = (By.XPATH, '/html/body/div/div/header/nav/a/p') # Кнопка личный кабинет


