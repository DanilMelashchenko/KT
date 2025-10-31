print("--- Task 1: Class Animal ---")

class Animal:
    # 1. Конструктор класу
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        print(f"New object created: {self.name}, {self.species}")

    # 2. Метод об’єкта
    def make_sound(self):
        if self.species == "Dog":
            print(f"{self.name} says: Woof! Woof!")
        elif self.species == "Cat":
            print(f"{self.name} says: Meow!")
        else:
            print(f"{self.name} (species: {self.species}) makes some sound.")

# Створення двох об’єктів (екземплярів) класу Animal
animal1 = Animal("Buddy", "Dog", 5)
animal2 = Animal("Whiskers", "Cat", 3)

# Виклик їхніх методів
animal1.make_sound()
animal2.make_sound()


# --- Завдання 2: Робота з об’єктами (Rectangle) ---
print("\n--- Task 2: Class Rectangle ---")

class Rectangle:
    # Конструктор
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Метод для обчислення площі
    def calculate_area(self):
        return self.width * self.height

# Створення двох об’єктів Rectangle
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)

# Обчислення та виведення площі
area1 = rect1.calculate_area()
area2 = rect2.calculate_area()

print(f"Area of rectangle 1 (10x5) = {area1}")
print(f"Area of rectangle 2 (7x3) = {area2}")

print("\n--- Task 1 (Inheritance): Class Vehicle ---")

# 1. Базовий (батьківський) клас
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"Vehicle created: {self.make} {self.model}")

# 2. Підклас Car, який наслідує Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"The engine of {self.model} ({self.fuel_type}) is started.")

# 3. Підклас Motorcycle, який наслідує Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        print(f"The motorcycle {self.model} performs a wheelie!")

# 4. Підклас Bicycle, який наслідує Vehicle
class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def ring_bell(self):
        print(f"The bicycle {self.model} rings: Ring-ring!")

my_car = Car("Toyota", "Camry", 2022, "Gasoline")
my_moto = Motorcycle("Harley-Davidson", "Sportster", 2019, False)
my_bike = Bicycle("Trek", "Marlin", 2023, 21)

print(f"Car: {my_car.make} {my_car.model}, Fuel: {my_car.fuel_type}")
my_car.start_engine()

print(f"Motorcycle: {my_moto.make} {my_moto.model}, Has sidecar: {my_moto.has_sidecar}")
my_moto.wheelie()

print(f"Bicycle: {my_bike.make} {my_bike.model}, Gears: {my_bike.num_gears}")
my_bike.ring_bell()


# --- Завдання 2 (Частина 2): Поліморфізм ---
print("\n--- Task 2 (Polymorphism): Method display_info ---")

# Повторне визначення класів для демонстрації поліморфізму
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # 1. Метод у базовому класі
    def display_info(self):
        print(f"This is a {self.make} {self.model} from {self.year}.")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"The engine of {self.model} ({self.fuel_type}) is started.")
    
    def display_info(self):
        print(f"[CAR]: {self.make} {self.model} ({self.year}), Fuel: {self.fuel_type}.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        print(f"The motorcycle {self.model} performs a wheelie!")
        
    def display_info(self):
        print(f"[MOTORCYCLE]: {self.make} {self.model} ({self.year}), Has sidecar: {self.has_sidecar}.")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def ring_bell(self):
        print(f"The bicycle {self.model} rings: Ring-ring!")
        
    def display_info(self):
        print(f"[BICYCLE]: {self.make} {self.model} ({self.year}), Gears: {self.num_gears}.")


# 3. Створення списку транспортних засобів різних типів
print("\nCreating a list of vehicles...")
vehicle_list = [
    Car("Ford", "Mustang", 1969, "Gasoline"),
    Motorcycle("Yamaha", "R1", 2021, False),
    Bicycle("Giant", "Talon", 2022, 18)
]
print("Calling display_info() for each object in the loop:")
for vehicle in vehicle_list:
    vehicle.display_info()
