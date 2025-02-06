import requests

target = input("Enter the target URL: ")

while True:
    try:
        response = requests.get(target)
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        break 
