from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Замените данными для вашей базы данных
DATABASE_URL = "postgresql://Skypro:12345678@localhost:5432/qa2"

# Создаем подключение
engine = create_engine(DATABASE_URL)

# Создаем сессию для работы с БД
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

# В случае необходимости, можно протестировать подключение
try:
    connection = engine.connect()
    print("Подключение успешно!")
except Exception as e:
    print(f"Ошибка подключения: {e}")
