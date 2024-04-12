from selenium.webdriver.common.by import By
class StellarburgersLocators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") #Кнопка войти в аккаунт на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href = '/account']") #Кнопка Личный Кабинет
    REGISTER_BUTTON = (By.XPATH, "//a[text() = 'Зарегистрироваться']") #Кнопка Зарегистрироваться при авторизации
    NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input") #Поле ввода имени при регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input") #Поле ввода почты при регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input") #Поле ввода пароля при регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']") #Кнопка Зарегистрироваться при регистрации
    ENTRANCE = (By.XPATH, "//h2[text() = 'Вход']") #Заголовок "Вход", появляющийся после успешной регистрации или выхода из учетной записи
    INVALID_PASSWORD = (By.XPATH, "//p[text() = 'Некорректный пароль']") #Надпись Некорректный пароль, при вводе невалидного пароля
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name = 'name']") #Поле ввода почты при авторизации
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name = 'Пароль']") #Поле ввода пароля при авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']") #Кнопка Войти при авторизации
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']") #Кнопка оформить заказ
    LOGIN_BUTTON_IN_REGISTRATION_OR_RECOVERY_FORM = (By.XPATH, "//a[text() = 'Войти']") #Кнопка Войти на странице формы регистрации
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль']") #Кнопка восстановить пароль
    TITLE_PROFILE = (By.XPATH, "//a[text() = 'Профиль']") #Заголовок поля Профиль
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@class = 'AppHeader_header__link__3D_hX' and @href = '/']/p[text() = 'Конструктор']") #Кнопка Конструктор
    LOGO_BUTTON = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']/a[@href = '/']") #Лого Stellar Burgers
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") #Кнопка выхода из профиля
    SAUCES_SECTION = (By.XPATH, "//span[text() = 'Соусы' and @class = 'text text_type_main-default']") #Секция соусы на странице конструктора
    TITLE_SAUCES_LIST = (By.XPATH, "//h2[text() = 'Соусы' and @class = 'text text_type_main-medium mb-6 mt-10']") #Заголовок списка соусов
    FILINGS_SECTION = (By.XPATH, "//span[text() = 'Начинки' and @class = 'text text_type_main-default']") #Секция начинки на странице конструктора
    TITLE_FILINGS_LIST = (By.XPATH, "//h2[text() = 'Начинки' and @class = 'text text_type_main-medium mb-6 mt-10']") #Заголовок списка начинок
    BUNS_SECTION = (By.XPATH, "//span[text() = 'Булки' and @class = 'text text_type_main-default']") #Секция Булки на странице конструктора
    TITLE_BUNS_LIST = (By.XPATH, "//h2[text() = 'Булки' and @class = 'text text_type_main-medium mb-6 mt-10']") #Заголовок списка булок





