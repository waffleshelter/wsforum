# **Для корректного запуска требуется:**
1) Создание virtual environment в папке Back
```
Python -m venv venv
```
2) .env файл в папке Back с содержимым вида:
```
DBROOT = 'sqlite+aiosqlite:///Back/database/db.sqlite3'
HASH_KEY = 'Here is hash key'
```
3) Установка всех библиотек из req.txt
```
pip install -r req.txt
```
