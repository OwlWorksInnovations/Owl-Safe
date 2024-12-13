import requests

def login(email, password, base_url='http://localhost:5000'):
    login_data = {
        'email': email,
        'password': password
    }
    response = requests.post(f'{base_url}/login-form', data=login_data, allow_redirects=False)
    
    if response.status_code in [200, 302]:
        jwt_token = response.cookies.get('jwt')
        return jwt_token
    return None

def get_app_passwords(jwt_token, base_url='http://localhost:5000'):
    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.post(f'{base_url}/auth', headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data['app_passwords']
    return None

def store_app_password(jwt_token, app_password, base_url='http://localhost:5000'):
    headers = {'Authorization': f'Bearer {jwt_token}'}
    payload = {'app_password': app_password}
    
    response = requests.post(f'{base_url}/store-app-password', 
                              headers=headers, 
                              json=payload)
    
    if response.status_code == 200:
        print("App password stored successfully")
        return True
    else:
        print(f"Failed to store app password: {response.json().get('message')}")
        return False

def main():
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    # Login and get JWT token
    jwt_token = login(email, password)
    
    if not jwt_token:
        print("Login failed")
        return None
    
    # Check existing app passwords
    app_passwords = get_app_passwords(jwt_token)
    
    if app_passwords:
        print(f"Existing App Passwords: {app_passwords}")
    
    # Option to store new app password
    store_new = input("Do you want to store a new app password? (y/n): ").lower()
    if store_new == 'y':
        new_app_password = input("Enter new app password: ")
        store_app_password(jwt_token, new_app_password)

if __name__ == "__main__":
    main()