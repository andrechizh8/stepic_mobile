

В данном проекте реализованы тесты  с использованием Appium + Android Studio, а также  сервиса browserstack:

:radio_button: Позитивная проверка авторизации на сайте

:radio_button: Негативная проверка авторизации на сайте

:radio_button: Добавление курса в избранное

:radio_button: Редактирование данных пользователя

:radio_button: Поиск курса 

Для запуска тестов локально необходимо :

    1. Настроить Android Studio

    2. Запустить Appium Server

    3. В файле .env определить логин и пароль для сайта www.stepik.org

    4. В командной строке Idea прописать :

        pip unstall poetry
        poetry lock
        poetry install
        env -S context="local" pytest .

![Альтернативный текст](https://github.com/andrechizh8/stepik_mobile/blob/main/readme%20files/stepik.gif)
---

Для запуск тестов с помощью browserstack необходимо:

1. В файле .env определить :
 
       1.1 Логин и пароль для сайта www.stepik.org
  
       1.2 Username и accesskey для browserstack
       
       1.3 Загрузить приложение stepik.apk в свой профиль на сайте www.browserstack.com и определить адрес приложения на сайте
       
       1.4 В командной строке прописать : 
       
            pip install poetry
            poetry lock
            poetry install 
            env -S context="browserstack" pytest .
            
![Альтернативный текст](https://github.com/andrechizh8/stepik_mobile/blob/main/readme%20files/stepik6.gif)
---

 ### Запуск в Jenkins : [JOB](https://jenkins.autotests.cloud/job/STEPIK/)
 
 Нажать на кнопку Собрать сейчас
![Альтернативный текст]([https://github.com/andrechizh8/ui_dns/blob/main/readme%20files/dns1.png](https://github.com/andrechizh8/stepik_mobile/blob/main/readme%20files/stepik1.png))

После сборки есть возможность посмотреть отчет с различными приложениями: 

Скриншот:

![Альтернативный текст](https://github.com/andrechizh8/stepik_mobile/blob/main/readme%20files/stepik2.png)


Кроме того, в проекте реализована возможность просмотр отчета в  Allure TestOps : 

![Альтернативный текст](https://github.com/andrechizh8/stepik_mobile/blob/main/readme%20files/stepik3.png)

И интеграция с Jira :

![Альтернативный текст](https://github.com/andrechizh8/stepik_mobile/blob/main/readme%20files/stepik4.png)

После прохождения тестов с использованием Jenkins в телеграмм приходит оповещение с результатами :

![Альтернативный текст](https://github.com/andrechizh8/stepik_mobile/blob/main/readme%20files/stepik7.png)
