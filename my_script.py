# script.py
import requests

url = "https://exptrackdata.onrender.com"
response = requests.get(url)

# You can print or process the response as needed
print(response.text)