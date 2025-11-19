from fastapi import FastAPI, HTTPException
from typing import Optional

# Створення екземпляра додатку
app = FastAPI()

# --- ЗАВДАННЯ 2 та 3: Базові маршрути ---

@app.get("/")
def read_root():
    return {"message": "Вітаємо у FastAPI!"}

@app.get("/about")
def about():
    return {"page": "Про нас", "description": "Інформація про сайт"}

@app.get("/contact")
def contact():
    return {
        "email": "d.melashchenko@htcolledge.sumdu.edu.ua",
        "phone": "+380665068497"
    }

# Додаємо власний маршрут /info (Завдання 3)
@app.get("/info")
def my_info():
    return {
        "developer": "Данил",
        "role": "Python Student",
        "language": "Python 3.10+"
    }


# --- ЗАВДАННЯ 4: Маршрути з параметрами ---

@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "name": f"Студент №{student_id}",
        "group": "КТ-24c"
    }

@app.get("/greeting/{name}")
def greet_user(name: str):
    return {"message": f"Привіт, {name}!"}


# --- ЗАВДАННЯ 5: Параметри запиту (Query Parameters) ---

@app.get("/search")
def search_items(query: str, limit: int = 10):
    return {
        "query": query,
        "limit": limit,
        "results": f"Знайдено результати для '{query}' (максимум {limit})"
    }


# --- ЗАВДАННЯ 6: Комбінування параметрів ---

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None, show_details: bool = False):
    result = {"item_id": item_id}
    
    if q:
        result["query"] = q
    if show_details:
        result["details"] = "Детальна інформація про товар"
    
    return result


# --- ЗАВДАННЯ 7: Калькулятор (Повна версія) ---

@app.get("/calc/add/{a}/{b}")
def add(a: float, b: float):
    return {"operation": "додавання", "result": a + b}

@app.get("/calc/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return {"operation": "віднімання", "result": a - b}

@app.get("/calc/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return {"operation": "множення", "result": a * b}

@app.get("/calc/divide/{a}/{b}")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Ділення на нуль неможливе"}
    return {"operation": "ділення", "result": a / b}

# Додаткове: Операція як параметр запиту
@app.get("/calc/operate")
def calculate(a: float, b: float, op: str):
    if op == "add":
        return {"result": a + b}
    elif op == "sub":
        return {"result": a - b}
    elif op == "mul":
        return {"result": a * b}
    elif op == "div":
        if b == 0: return {"error": "Ділення на нуль"}
        return {"result": a / b}
    else:
        return {"error": "Невідома операція"}


# --- ЗАВДАННЯ 8: API для студентів ---

# Тимчасове сховище даних
students_db = {
    1: {"name": "Іван Петренко", "group": "KT-24c", "grade": 90},
    2: {"name": "Марія Коваленко", "group": "КТ-23", "grade": 85},
    3: {"name": "Петро Сидоренко", "group": "KT-23", "grade": 88},
    4: {"name": "Данил Мелащенко", "group": "KT-24c", "grade": 95},
    5: {"name": "Олена Нездала", "group": "KT-23", "grade": 59}
}

@app.get("/students")
def get_all_students():
    return students_db

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    if student_id in students_db:
        return students_db[student_id]
    return {"error": "Студента не знайдено"}

@app.get("/students/group/{group_name}")
def get_students_by_group(group_name: str):
    result = {}
    for sid, student in students_db.items():
        if student["group"] == group_name:
            result[sid] = student
    return result

# Пошук студентів з оцінкою вище заданої
@app.get("/students/filter/grade")
def get_students_by_min_grade(min_grade: int):
    result = {}
    for sid, student in students_db.items():
        if student["grade"] >= min_grade:
            result[sid] = student
    
    if not result:
        return {"message": "Студентів з таким високим балом немає"}
    return result