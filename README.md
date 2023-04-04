Какие тесты присутствуют в файле
----------------
1. Проверка наличия на странице всех необходимых элементов
2. Проверка поведения табов логина
3. Позитивные и негативные тесты на вход по телефону/емейлу/логину/паролю


Как запустить тесты
----------------

1) Установить все требования:

    ```bash
    pip3 install -r requirements
    ```

2) Установить веб драйвер хрома https://chromedriver.chromium.org/downloads

3) Запустить тесты следующими командами:

    ```bash
     pytest -v -m "UI" --driver Chrome --driver-path chromedriver.exe - Для запуска тестов UI
     pytest -v -m "positive" --driver Chrome --driver-path chromedriver.exe - Для запустка позитивных тестов логина
     pytest -v -m "negative" --driver Chrome --driver-path chromedriver.exe - Для запуска негативных тестов логина
     pytest -v -m "login" --driver Chrome --driver-path chromedriver.exe - Для запуска тестов на форму логина
    ```

