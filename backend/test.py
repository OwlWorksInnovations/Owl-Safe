# Just to test the auth backend with backend.py
import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/authorize"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())
