import requests

url = 'https://httpbin.org/get'

# Створюємо словник з параметрами
params = {
    'user': 'danyl',
    'status': 'active'
}

try:
    # Передаємо параметри у функцію get()
    response = requests.get(url, params=params)
    
    # Використовуємо .json() для автоматичної розшифровки JSON
    print("--- Ansver format JSON ---")
    print(response.json())

    print("\n--- URL, which was requested ---")
    print(response.url)

except requests.exceptions.RequestException as e:
    print(f"Сталася помилка під час запиту: {e}")