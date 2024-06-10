<h1 align="center">TGSB - SMS bomber. TG bot service written in python and aiogram</h1>
<h3 align="center">!!! Use at your own risk. The developer is not responsible for your actions !!!</h3>

<div class="badges" align="center">
    <a href="./LICENSE.md"><img  class="badge" src="https://img.shields.io/github/license/Nighty3098/TGSB?style=for-the-badge&color=a6e0b8&logoColor=ffffff&labelColor=1c1c29"  style="border-radius: 5px;"/></a>
    <br><br>
	<a href="https://discord.gg/tnHSEc2cZv"><img src="https://invidget.switchblade.xyz/r8jWX8ugDd" style="border-radius: 15px;"/></a><br><br>
	<a href="https://discord.gg/#9707" target="blank"><img src="https://img.shields.io/badge/Discord-%237589d5.svg?style=for-the-badge&logo=discord&logoColor=black"/></a>
	<a href="https://t.me/Night3098" target="blank"><img src="https://img.shields.io/badge/Telegram-7dc4e4?style=for-the-badge&logo=telegram&logoColor=black"/></a>
	<a href="mailto:night3098game@gmail.com" target="blank"><img src="https://img.shields.io/badge/Gmail-f5a7a0?style=for-the-badge&logo=gmail&logoColor=black"/></a>
	<a href="https://www.reddit.com/user/Night3098" target="blank"><img src="https://img.shields.io/badge/Reddit-f5a7a0?style=for-the-badge&logo=reddit&logoColor=black"/></a>
	<br><br>
	<img src="https://img.shields.io/github/created-at/Nighty3098/TGSB?style=for-the-badge&color=7dc4e4&logoColor=D9E0EE&labelColor=1c1c29" style="border-radius: 5px;">
	<img class="badge" src="https://img.shields.io/github/last-commit/Nighty3098/TGSB?style=for-the-badge&color=7dc4e4&logoColor=D9E0EE&labelColor=1c1c29" style="border-radius: 5px;"/>
	<img class="badge" src="https://img.shields.io/github/issues-pr/Nighty3098/TGSB?style=for-the-badge&color=ef9f9c&logoColor=85e185&labelColor=1c1c29" style="border-radius: 5px;" />
	<img class="badge" src="https://img.shields.io/github/repo-size/Nighty3098/TGSB?style=for-the-badge&color=ea9de7&logoColor=D9E0EE&labelColor=171b22" style="border-radius: 5px;"/>
	<img class="badge" src="https://img.shields.io/github/issues/Nighty3098/TGSB?style=for-the-badge&color=dbb6ed&logoColor=ffffff&labelColor=1c1c29"  style="border-radius: 5px;"/>
	<img src="https://img.shields.io/github/commit-activity/t/Nighty3098/TGSB?style=for-the-badge&color=a6e0b8&logoColor=D9E0EE&labelColor=171b22" style="border-radius: 5px;"/>
	<img src="https://img.shields.io/github/languages/count/Nighty3098/TGSB?style=for-the-badge&color=ea9de7&logoColor=D9E0EE&labelColor=171b22" style="border-radius: 5px;"/>
	<img class="badge" src="https://img.shields.io/github/stars/Nighty3098/TGSB?style=for-the-badge&color=eed49f&logoColor=D9E0EE&labelColor=1c1c29" style="border-radius: 5px;"/>
	<img class="badge" src="https://img.shields.io/github/forks/Nighty3098/TGSB?style=for-the-badge&color=9dc3ea&logoColor=D9E0EE&labelColor=1c1c29"  style="border-radius: 5px;"/>
	<br><br>
	<img class="badge" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=black&color=7dc4e4" style="border-radius: 5px;"/>
	<img class="badge" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=black&color=7dc4e4" style="border-radius: 5px;"/>
</div>

<h2 align="center">Functional:</h2>


<h3 align="center">For users</h3>
 - btn - "SMA spam"
 - btn - "Call spam"


<h3 align="center">For admins</h3>

- /adduser %user_id% - Add user to whitelist
- /removeuser %user_id% - Remove user from whitelist
- /addadmin %admin_id% - Add admin
- /removeadmin %admin_id% - Remove admin
- /whitelist - Send whitelist

- btn - "SMS spam"
- btn - "Call cpam"


<h3 align="center">For creator</h3>

- /addadmin %admin_id% - Add adnim
- /removeadmin %admin_id% - Remove admin
- /adduser %user_id% - Add user to whitelist
- /removeuser %user_id% - Remove user from whitelist
- /whitelist - Send whitelist
- /block %user_id% - Block user
- /unblock %user_id% - Unblock user

- btn - "Service control" : 
    - btn - "sys stats"
    - btn - "logs"
    - btn - "clear log"
    - btn - "off"
    - btn - "on"

- btn - "SMS spam"
- btn - "Call cpam"

<h1 align="center">Structure</h1>

```
.
├── config.py
├── create_requirements.sh
├── data
│   ├── data.json
│   └── names.txt
├── handlers.py
├── keyboards
│   ├── admin.py
│   ├── dev.py
│   ├── service.py
│   └── user.py
├── LICENSE
├── logs
│   └── TGSB.log
├── main.py
├── MESSAGES_TEXT.py
├── README.md
├── requirements.txt
├── spam
│   ├── gen_user_data.py
│   ├── mask.py
│   ├── proxy.py
│   └── spam.py
└── validate.py
```

<h1 align="center">Dependencies</h1>

```
aiofiles==23.2.1
aiogram==3.3.0
aiogram-dialog==2.1.0
aiohttp==3.9.3
aiosignal==1.3.1
annotated-types==0.6.0
anyio==4.2.0
attrs==23.2.0
cachetools==5.3.2
certifi==2024.2.2
charset-normalizer==3.3.2
colorama==0.4.6
docopt==0.6.2
frozenlist==1.4.1
h11==0.14.0
httpcore==1.0.2
httpx==0.25.2
idna==3.6
Jinja2==3.1.3
loguru==0.7.2
magic-filter==1.0.12
MarkupSafe==2.1.5
multidict==6.0.5
pipreqs==0.4.13
pretty-errors==1.2.25
psutil==5.9.8
pydantic==2.5.3
pydantic_core==2.14.6
python-telegram-bot==20.7
requests==2.31.0
six==1.16.0
sniffio==1.3.0
typing_extensions==4.9.0
urllib3==2.2.0
user_agent==0.1.10
yarg==0.1.9
yarl==1.9.4
```

<h1 align="center">Installing</h1>


```
git clone https://github.com/Nighty3098/TGSB 
cd TGSB

python3 -m venv TGSB
source TGSB/bin/activate

pip3 install -r requirements.txt

TGSB_TOKEN=%токен_вашего_бота% python3 main.py
```


