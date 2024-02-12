<h1 align="center">  TGSM - телеграм сервис смс спама </h1>
<h2 align="center">Команды:</h2>



<h3 align="center">Для пользователей</h3>

- /spam - Спам смс
- /call - Спам звонками
- /admin - Обратиться к администратору


<h3 align="center">Для администратора</h3>

- /adduser - Добавить пользователя в белый список
- /removeuser - Удалить пользователя из белого списка 
- /whitelist - Вывести содержимое whitelist\
- /spam - Спам смс
- /call - Спам звонками


<h3 align="center">Для создателя</h3>

- /adduser - Добавить пользователя в белый список
- /removeuser - Удалить пользователя из белого списка 
- /whitelist - Вывести содержимое whitelist\
- /spam - Спам смс
- /call - Спам звонками
- /off - Выключить бота (отключить доступ для всех пользователей)
- /on - Восстановить доступ к боту для всех пользователей
- /all_users - Вывести всех пользователей, которые запускали бота
- Дополнительное меню в виде InlineKeyboard с кнопками для вывода информации о сервисе, использовании ресурсов сервера, токенах, данных.


<h1 align="center">Структура проекта</h1>


```

```

<h1 align="center">Зависимости для проекта</h1>

- aiofiles==23.2.1
- aiogram==3.3.0
- aiogram-dialog==2.1.0
- aiohttp==3.9.3
- aiosignal==1.3.1
- annotated-types==0.6.0
 - anyio==4.2.0
- attrs==23.2.0
- cachetools==5.3.2
- certifi==2024.2.2
- charset-normalizer==3.3.2
- colorama==0.4.6
- docopt==0.6.2
- frozenlist==1.4.1
- h11==0.14.0
- httpcore==1.0.2
- httpx==0.25.2
- idna==3.6
- Jinja2==3.1.3
- loguru==0.7.2
- magic-filter==1.0.12
- MarkupSafe==2.1.5
- multidict==6.0.5
- pipreqs==0.4.13
- pretty-errors==1.2.25
- psutil==5.9.8
- pydantic==2.5.3
- pydantic_core==2.14.6
- python-telegram-bot==20.7
- requests==2.31.0
- sniffio==1.3.0
- typing_extensions==4.9.0
- urllib3==2.2.0
- yarg==0.1.9
- yarl==1.9.4

<h1 align="center">Установка и использование</h1>


```
git clone https://github.com/Nighty3098/TGSB 
cd TGSB

python3 -m venv TGSB
source TGSB/bin/activate

pip3 install -r requirements.txt

TGSB_TOKEN=%токен_вашего_бота% python3 main.py
```


