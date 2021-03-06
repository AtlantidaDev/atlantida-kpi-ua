# atlantida-kpi-ua

## Запуск локально

1. Встановити [Python 3.6](https://www.python.org/downloads/)
   
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
    python3 -m pip install virtualenv
    ```
    
    - *Console command for Linux/Mac*
    ```commandline
    python3 -m pip install virtualenv
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
    python3 -m virtualenv env
    env\Scripts\activate.bat
    pip install -r requirements-local.pip
    python manage.py runserver
    ```

    - *Console command for Linux/Mac*
    ```commandline
    python3 -m virtualenv env
    source env/bin/activate
    pip install -r requirements-local.pip
    python manage.py runserver
    ```
7. Тепер відкрийте браузер і перейдіть на сторінку
    [http://localhost:8000/](http://localhost:8000/).
    Якщо все зроблено правильно, ви маєте побачити сторінку index.html


## Frontend code style

Для фронтенда мы используемого методологию БЭМ (Блок Элемент Модификатор)

пример:

### Блоки:
- "Про нас" - about-us

### Элементы
- "Статья про нас"			  about-us__article
- "Заголовок статьи про нас"		  about-us__article-title
- "Содержание статьи про нас"		  about-us__article-description
- "Кнопка для статьи про нас" 		  about-us__article-button

### Модификаторы 

Стиль для кнопки можно создать как независимый от блока "about-us", а сделать модификатор для блока "button"
- "Кнопка для статьи про нас" button_about-us

Определение перечня классов во стором случае выглядит гармоничнее чем в первом
- class="button about-us__article-button" 
- class="button button_about-us"
	
Как это будет выглядеть в html и css:
```html
<div class="about-us">
    <div class="about-us__article">
        <h1 class="about-us__article-title">About us</h1>
        <p class="about-us__article-description">Description text</p>
        <a class="button about-us__article-button" href="#">Read more</a>
	<a class="button button_about-us" href="#">Read more</a>
    </div>
    <div class="about-us__photos">
        <img class="about-us__photos-img_0">
        <img class="about-us__photos-img_1">
    </div>
</div>
```
### !!!ВАЖНО!!! Вложенность элеметнов в элементы в методологии БЭМ запрещена!
about-us__article__button - подобных классов быть не должно


[See](https://ru.bem.info/methodology/key-concepts/)
