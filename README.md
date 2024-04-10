Проект тестирует UI сайта https://stellarburgers.nomoreparties.site/ 
В файле conftest.py лежат фикстуры
В файле data.py лежат тестовые данные
В файле locators.py лежат локаторы
В файле settings.py лежат настройки
В папке tests лежат файлы с тестами. На каждую проверку один файл.
Проверка регистрации - файлы: 
test_registration.py
test_invalid_password.py
Проверка входа:
test_auth_from_button_in_registration_form.py
test_auth_from_login_button.py
test_auth_from_personal_account.py
test_auth_from_recover_password.py
Проверка перехода в личный кабинет:
test_switch_to_personal_account.py
Проверка перехода из личного кабинета в конструктор:
test_switch_to_constructor_from_constructor_button.py
test_switch_to_constructor_from_logo.py
Проверка выхода из аккаунта:
test_logout_from_personal_account.py
Проверка перехода между разделами в конструкторе:
test_go_to_buns_section.py
test_go_to_filings_section.py
test_go_to_sauces_section.py

Запустить тесты из терминала можно командой: pytest -v tests






