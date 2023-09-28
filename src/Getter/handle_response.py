def handle_response(response):    
    if response.status_code == 200:
        return response
    else:
        error_response = {
            "status_code": response.status_code,
            "content": response.content.decode('utf-8')  # Convert bytes to string
        }
        return error_response