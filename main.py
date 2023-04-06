## Request and classes

import requests
from classes import *


url = 'https://jsonplaceholder.typicode.com/users'
user_obj = []
response = requests.get(url)
user_data = response.json()
requesting = True


while requesting:
    # Get input for the user
    username = input("Enter User Name for start searching data (or 'q' to quit): ").lower()
    for user_res in user_data:
        user = MyUser(user_res['id'], user_res['email'], user_res['username'], user_res['name'], user_res['address'])
        user_obj.append(user)              ## Create object to user
    if username == 'q':                    ## Check if user wants to quit
        requesting = False
        continue        

    # Search for user
    found_user = False
    for user in user_obj:
        if user.username.lower() == username:
            print(user.info())
            found_user = True
            break

    if not found_user:
        print(f'User with username "{username}" not found')
print("System shoutdown")