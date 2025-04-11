# **Для корректного запуска требуется:**
1) Создание зависимостей 
### Windows
```
cd backend
Python -m venv venv
venv/scripts/activate
pip install -r req.txt
```
### Linux
```
Source backend
Python -m venv venv
venv/scripts/activate
pip install -r req.txt
```

2) Создание .env файл в папке backend/src с содержимым вида:
```
DBROOT = 'sqlite+aiosqlite:///src/db.sqlite3'
HASH_KEY = 'Here is hash key'
FPATH = '(диск):/wsforum/frontend/'
```
3) Запуск backend`a
```
Python -m src.main
```#   t e s t d e p l o y 
 
 
