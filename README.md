# **Для корректного запуска требуется:**
1) Создание зависимостей
```
Python -m venv venv
venv/scripts/activate
pip install -r req.txt
```
2) Создание .env файл в папке src с содержимым вида:
```
DBROOT = 'sqlite+aiosqlite:///Back/database/db.sqlite3'
HASH_KEY = 'Here is hash key'
```
3) Запуск приложения
```
Python -m src.main
```