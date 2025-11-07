import requests
from requests.exceptions import RequestException # Import the specific exception

url_to_fetch = 'https://www.google.com'
output_filename = 'google_homepage.html'

print(f"Requesting {url_to_fetch}...")

try:
    # --- TASK 1 (modified): Perform the request ---
    response = requests.get(url_to_fetch, timeout=5) 

    # --- TASK 5 (part 1): HTTP Error Handling ---
    response.raise_for_status() 

    # --- TASK 4: Handling the Response ---
    print("\n--- Response Headers (partial) ---")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    print(f"Server: {response.headers.get('Server')}")
    print(f"Date: {response.headers.get('Date')}")

    print("\n--- Response Content (first 300 chars) ---")
    print(response.text[:300] + "...")

    # --- TASK 6: Saving Content to a File ---
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
        
    print(f"\n[Success] Content saved to file: {output_filename}")


# --- TASK 5 (part 2): General Error Handling ---
except RequestException as e:
    print(f"\n[Error] Request failed: {e}")