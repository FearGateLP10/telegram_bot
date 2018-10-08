Telegram-bot
============

Telegram-bot создан и модифицируется в течение обучения в `Learn Python`_ .
На данный момент реализован следующий функцонал:
приветствие, получение фото котиков при запросе, ephem, эхо-ответ на любые текстовые сообщения.

Установка
---------

Активируйте виртуальное окружение, затем установите зависимости:

.. code-block:: text
	pip install -r requirements.txt

Поместите фото котиков в папку images в формате jpg, названия файлов должны начинаться c cat, например: cat_in_black.jpg

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

    PROXY = {'proxy_url': 'socks5://ВАШ_SOCKS5_ПРОКСИ:1080',
            'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 'password': 'ПАРОЛЬ'}}

    API_KEY = 'API ключ, котрый вы получили у BotFather'

    USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']

Запуск
------

В активированном виртуальном окружении выполните:

.. code-block:: text

    python3 bot.py

Пример
------

.. code-block:: text
	/start
	/cat
	/ephem Mars
	Hi!

***

.. _Learn Python: https://learn.python.ru/