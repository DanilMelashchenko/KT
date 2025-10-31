import math
from abc import ABC, abstractmethod

print("--- Task 1: Encapsulation ---")

class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__password = None

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def set_name(self, new_name):
        if len(new_name) > 1:
            self.__name = new_name
        else:
            print("Error: Name must be longer than 1 character.")
            
    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.__email = new_email
        else:
            print("Error: Invalid email format.")

    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Password set successfully.")
        else:
            print("Error: Password must be 8 characters or longer.")
    
    def check_password(self, password_to_check):
        if self.__password is None:
            return "Password has not been set yet."
            
        return self.__password == password_to_check

user1 = User("Danylo", "danylo@example.com")

print(f"Username: {user1.get_name()}")
print(f"User email: {user1.get_email()}")

user1.set_name("Danylo Oleksandrovych")
print(f"New name: {user1.get_name()}")

user1.set_password("my_super_secret_123")

print(f"Checking password 'wrong_pass': {user1.check_password('wrong_pass')}")
print(f"Checking password 'my_super_secret_123': {user1.check_password('my_super_secret_123')}")

print("\n--- Task 2: Abstraction ---")

class Shape(ABC):
    
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass
        
    def display_info(self):
        print(f"This is a shape of type: {self.name}")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
        
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        
    def calculate_area(self):
        return 0.5 * self.base * self.height

rect = Rectangle(10, 5)
circ = Circle(7)
tri = Triangle(8, 4)

shapes = [rect, circ, tri]

for shape in shapes:
    shape.display_info()
    area = shape.calculate_area()
    print(f"Area of shape '{shape.name}' = {area:.2f}")
    print("-" * 20)