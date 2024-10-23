import requests

# Step 1: Get JWT Token
token_url = 'http://127.0.0.1:8000/api/token/'
token_data = {
    'username': 'kishore',
    'password': 'kishore346'
}

token_response = requests.post(token_url, json=token_data)
token = token_response.json().get('access')

print(token)

# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5Njc2MDg2LCJpYXQiOjE3Mjk2NzQyODYsImp0aSI6ImZhZWUwMzJhMjI0ZDQxZWI4ZDJhM2NjMTdhOGQ0NmM4IiwidXNlcl9pZCI6MX0.vy_u6ot3ZqUz03i0tgpmYCGnYk02gFzfiSRC6SnQFxU"
# # Step 2: Use the token to create an item
# url = 'http://127.0.0.1:8000/api/items/'
# headers = {
#     'Authorization': f'Bearer {token}',
#     'Content-Type': 'application/json'
# }
#
# data = {
#     'name': 'Item2',
#     'description': 'A sample item description three'
# }
#
# response = requests.post(url, json=data, headers=headers)
# print(response.status_code)
# print(response.json())

# acesstoken::eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5Njc2MDg2LCJpYXQiOjE3Mjk2NzQyODYsImp0aSI6ImZhZWUwMzJhMjI0ZDQxZWI4ZDJhM2NjMTdhOGQ0NmM4IiwidXNlcl9pZCI6MX0.vy_u6ot3ZqUz03i0tgpmYCGnYk02gFzfiSRC6SnQFxU


# Replace '1' with the actual ID of the item you want to retrieve
url = 'http://127.0.0.1:8000/api/items/1/'
headers = {
    'Authorization': f'Bearer {token}'
}

# GET request to retrieve an item
response = requests.get(url, headers=headers)
print(response.status_code)  # Expecting 200
print(response.json())  # Should print the item details
