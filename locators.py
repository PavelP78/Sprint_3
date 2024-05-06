from selenium.webdriver.common.by import By

class StellarBurgersLocators:

    PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/following::input[1]') # Поле пароль
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following::input[1]') # Поле е-майл
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//nav/a[@class='AppHeader_header__link__3D_hX']") # Кнопка личный кабинет
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]') # Кнопка войти
    MAIN_ENTER_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти в аккаунт на главной
    ENTER_BUTTON_REGISTRATION_FORM = (By.XPATH, '//a[text()="Войти"]') # Кнопка войти  в форме регистрации
    BUTTON_PASSWORD_RECOVERY_FORM = (By.XPATH, '//a[text()="Восстановить пароль"]') # Кнопка  восстановления пароля
    ENTER_BUTTON_PASSWORD_RECOVERY_FORM = (By.XPATH, '//a[text()="Войти"]') # Кнопка войтив форме восстановления пароля
    REGISTRATION_BUTTON = (By.XPATH, '//a[text()="Зарегистрироваться"]') # Кнопка зарегистрироваться
    DESIGNER_BUTTON = (By.XPATH, '//p[text()="Конструктор"]') # Кнопка конструктор
    LOGO_BUTTON = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]') # Логотип Stellar Burgers
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]') # Кнопка «Выход» в личном кабинете
    ROLLS_BUTTON = (By.XPATH, '//span[text()="Булки"]') # Кнопка «Булки»
    SOUCE_BUTTON = (By.XPATH, '//span[text()="Соусы"]') # Кнопка «Соусы»
    FILLING_BUTTON = (By.XPATH, '//span[text()="Начинки"]') # Кнопка «Начинки»
    ENTER_BUTTON_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]') # Кнопка войти в аккаунт
    ERROR_PASSWORD= (By.XPATH, '//p[text()="Некорректный пароль"]') # Надпись некорректный пароль
    ORDER_BUTTON= (By.XPATH, '//button[text()="Оформить заказ"]') # Кнопка оформить заказ
    NAME_FIELD = (By.XPATH, '//label[text()="Имя"]/following::input[1]') # Поле имя при регистрации
    EMAIL_FIELD_REGISTRATION = (By.XPATH, '//label[text()="Email"]/following::input[1]') # Поле е-майл при регистрации
    PASSWORD_FIELD_REGISTRATION = (By.XPATH, '//label[text()="Пароль"]/following::input[1]') # Поле пароль при регистрации
    REGISTRATION_BUTTON_REGISTRATION = (By.XPATH, '//button[text()="Зарегистрироваться"]') # Кнопка зарегистрироваться на странице регистрации
    ERROR_PASSWORD_REGISTRATION= (By.XPATH, '//p[text()="Некорректный пароль"]') # Надпись некорректный пароль на странице регистрации
    ROLLS_PICTURE = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]') # Картинка флюоресцентная булка
    ROLLS_ELEMENT = (By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]') # Меню булки после клика на Булки
    SOUCE_PICTURE = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]') # Картинка соус Spisy-x
    FILLING_PICTURE = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]') # Картинка начинки говяжий метеорит
    SAVE_BUTTON= (By.XPATH, '//button[text()="Сохранить"]') # Кнопка сохранить

