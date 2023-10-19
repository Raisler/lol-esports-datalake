import requests

def handle_response(response):    
    if response.status_code == 200:
        return response
    else:
        error_response = {
            "status_code": response.status_code,
            "content": response.content.decode('utf-8')  # Convert bytes to string
        }
        print(error_response)
        return response
    
def is_internet_available():
    try:
        # Try to send a simple HTTP request to a known reliable server
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False