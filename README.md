1. Устноваить зависимости

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
# открыть новый терминал после этого

micromamba env create -f env.yml
micromamba activate new-env
pip install pyTelegramBotAPI
```

2. Создать бота в @BotFather (https://t.me/BotFather)
3. Скопировать его токен в .env TOKEN=""
4. Запустить бота

```bash
python main.py
```
