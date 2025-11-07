import requests

url = 'https://httpbin.org/get'

try:
    response = requests.get(url)

    print("--- Response content (response.text) ---")
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request.: {e}")