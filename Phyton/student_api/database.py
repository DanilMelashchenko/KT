from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"

# Створення движка бази даних
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Створення сесії для роботи з БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовий клас для моделей
Base = declarative_base()

# Функція для отримання сесії БД (Dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()