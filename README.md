# atlantida-kpi-ua

## Запуск локально

1. Встановити [Python 2.7](https://www.python.org/downloads/)
2. Встановити [PIP](https://pip.pypa.io/en/stable/installing/)
3. За допомогою PIP завантажити модуль virtualenv

    - *Console command for Windows Machine*
    ```commandline
    python -m pip install virtualenv
    ```
    
    - *Console command for Linux/Mac*
    ```commandline
    pip install virtualenv
    ```

4. Зробити собі Форк репозиторія
5. Зклонувати репозиторій на свій локальний комп'ютер
6. З консолі перейти в папку, куди ви зклонували репозиторій
    і запустити наступні команди:
    
    - *Console command for Windows Machine*
    ```commandline
    python -m virtualenv env
    env\bin\activate.bat
    python -m pip install -r requirements-local.pip
    python manage.py runserver
    ```

    - *Console command for Linux/Mac*
    ```commandline
    virtualenv env
    source env/bin/activate
    pip install -r requirements-local.pip
    python manage.py runserver
    ```
7. Тепер відкрийте браузер і перейдіть на сторінку
    [http://localhost:8000/](http://localhost:8000/).
    Якщо все зроблено правильно, ви маєте побачити сторінку index.html