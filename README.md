# atlantida-kpi-ua

## Запуск локально

1. Встановити [Python 2.7](https://www.python.org/downloads/)
   
   Для Windows:
   - *Додати enviroment variable*
   ```commandline
    This PC -> Properties -> Advanced system settings -> Advanced
	-> (Button) Enviroment Variables... -> System variables 
	-> (Double click) Path -> New -> Insert your path to python
	For example: C:\Python27 -> Click OK
    ```
	[See](https://www.nextofwindows.com/how-to-addedit-environment-variables-in-windows-7)
   
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
	
	```commandline
	git clone https://github.com/YOUR-USERNAME/atlantida-kpi-ua.git
    cd atlantida-kpi-ua
	git remote add upstream https://github.com/AtlantidaDev/atlantida-kpi-ua
	git fetch upstream
	git checkout master
	git merge upstream/master
	git checkout -b dev
	git merge upstream/dev
    ```
	
	[Fork A Repo](https://help.github.com/articles/fork-a-repo/)
	[Syncing a fork](https://help.github.com/articles/syncing-a-fork/)

6. З консолі перейти в папку, куди ви зклонували репозиторій
    і запустити наступні команди:
    
    - *Console command for Windows Machine*
    ```commandline
    python -m virtualenv env
    env\Scripts\activate.bat
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