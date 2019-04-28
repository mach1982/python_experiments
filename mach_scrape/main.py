import requests

url_address = input("Enter URL")

response= requests.get('http://' + url_address)

if response.status_code == 200:
    print("Success")