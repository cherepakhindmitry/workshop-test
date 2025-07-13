# Импорт движка и сессии из SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL для подключения к базе данных PostgreSQL
DATABASE_URL = "postgresql://Skypro:12345678@localhost:5432/qa2"

# Создание движка
engine = create_engine(DATABASE_URL)

# Создание сессии для взаимодействия с БД
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Проверка подключения (необязательно, но полезно при отладке)
try:
    connection = engine.connect()
    print("Подключение успешно!")
except Exception as e:
    print(f"Ошибка подключения: {e}")
