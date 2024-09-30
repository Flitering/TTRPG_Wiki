# TTRPG Wiki

Веб-портал для игроков и мастеров Pathfinder на Django.

## Функциональность

- Просмотр и добавление материалов
- Создание и управление персонажами
- Изучение правил игры

## Установка

```bash
git clone https://github.com/<your_username>/TTRPG_Wiki.git
cd TTRPG_Wiki
python -m venv venv
venv\Scripts\activate  # Для Windows
# source venv/bin/activate  # Для macOS/Linux
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
(В проекте отсутствует папка CSS, её нужно сделать вручную чтобы не было ошибок)