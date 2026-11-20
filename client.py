import requests

URL = "http://127.0.0.1:8001"

user_credentials={
  "username": "melvin",
  "password": "melvin",
  "user_type": "admin"
}

response = requests.post(url=URL + "/register",json=user_credentials)
print(response.json())
print(response)
print(response.status_code)

response = requests.post(url=URL + "/login",json=user_credentials)
print(response.json())
print(response)

response_json=response.json()
access_token=response_json["access_token"]
refresh_token=response_json["refresh_token"]


header={"token": access_token}
response=requests.get(url=URL + "/packages" ,headers=header)
print(response.json())


get_id= 1
header={"token": access_token}
response=requests.get(url=URL + "/packages" + f"/{get_id}", headers=header)
print(response.json())


status={ "status": "received"}
header={"token": access_token}
response=requests.patch(url=URL + "/packages" + f"/{get_id}",json=status, headers=header)
print(response.json())