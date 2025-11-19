from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print(pwd_context.hash("Busya123"))
print(pwd_context.hash("Princesska123"))