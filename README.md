1. Устноваить зависимости

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
# открыть новый терминал после этого

micromamba env create -f env.yml
micromamba activate new-env
pip install pyTelegramBotAPI
```
2. Установить полезные плагины: VSCode - Расширения - Фильтрация - Рекомендованные для воркспейса
3. Создать бота в @BotFather (https://t.me/BotFather)
4. Скопировать его токен в .env TOKEN=""
5. Запустить бота

```bash
python main.py
```
