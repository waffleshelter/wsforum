# **Для корректного запуска требуется:**
## 1) Создание зависимостей

**Windows**
```
Python -m venv venv
venv/scripts/activate
pip install -r req.txt
```
**Linux**
```
Source backend
Python -m venv venv
venv/scripts/activate
pip install -r req.txt
```
## 2) Создание .env файл в папке src с содержимым вида:
```
DBROOT = 'sqlite+aiosqlite:///src/db.sqlite3'
HASH_KEY = 'Here is hash key'
```
## 3) Запуск приложения
```
Python -m src.main
```
