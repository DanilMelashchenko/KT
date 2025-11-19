from datetime import datetime, timedelta
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt

# --- НАЛАШТУВАННЯ ---

# Секретний ключ для підпису токенів (у реальному проєкті це довгий випадковий рядок)
SECRET_KEY = "my_super_secret_key_change_me_please"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(title="JWT Auth Example")

# Налаштування для хешування паролів
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Схема авторизації (вказуємо, що URL для отримання токена це "/token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- ФЕЙКОВА БАЗА ДАНИХ ---
# Пароль для обох користувачів: "secret"
# Хеш згенеровано через pwd_context.hash("secret")
fake_users_db = {
    "danyl": {
        "username": "danyl",
        "full_name": "Данил Студент",
        "email": "danyl@example.com",
        "hashed_password": "$2b$12$aF5t2ZzooS21tA/wta0MzO4f0oomip1TN6VOKfdoYCklh8uOxvjMy",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderland",
        "email": "alice@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga311W",
        "disabled": False,
    },
}

# --- МОДЕЛІ ДАНИХ ---

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

# --- ДОПОМІЖНІ ФУНКЦІЇ ---

def verify_password(plain_password, hashed_password):
    """Перевіряє, чи співпадає введений пароль з хешем у БД"""
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str):
    """Дістає користувача з 'бази даних'"""
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Генерує JWT токен"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    # Додаємо час закінчення дії токена
    to_encode.update({"exp": expire})
    # Кодуємо токен
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Ця функція — 'охоронець'. Вона перевіряє токен.
    Якщо токен валідний — повертає користувача.
    Якщо ні — викидає помилку 401.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не вдалося перевірити облікові дані",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Декодуємо токен
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# --- МАРШРУТИ (ENDPOINTS) ---

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Маршрут для входу. Приймає username та password.
    Повертає JWT токен.
    """
    user = get_user(fake_users_db, form_data.username)
    
    # Перевірка користувача та пароля
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Невірний логін або пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Якщо все ок, створюємо токен
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    ЗАХИЩЕНИЙ МАРШРУТ.
    Доступний тільки якщо є валідний токен.
    Повертає інформацію про поточного користувача.
    """
    return current_user

@app.get("/public")
async def read_public():
    """Публічний маршрут, доступний всім"""
    return {"message": "Ця інформація доступна всім без реєстрації"}