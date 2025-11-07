import requests

url = 'https://httpbin.org/get'

try:
    response = requests.get(url)
    
    print("--- Вміст відповіді (response.text) ---")
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Сталася помилка під час запиту: {e}")