import requests

response = requests.get('https://thawing-garden-09505.herokuapp.com/assessment/22')
print(response)
print(response.json())