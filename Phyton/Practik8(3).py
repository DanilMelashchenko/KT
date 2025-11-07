import requests

url = 'https://httpbin.org/post'

data_to_send = {
    'username': 'danyl_python',
    'password': 'my_secret_password'
}

try:
    # Виконуємо POST-запит, передаючи дані через параметр 'data'
    response = requests.post(url, data=data_to_send)
    
    # httpbin.org/post поверне нам JSON, де в полі "form" будуть наші дані
    print("--- answer is in the format JSON ---")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request.: {e}")