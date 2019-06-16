import requests
from bs4 import BeautifulSoup
res=requests.get('https://aadesh.pythonanywhere.com/myapp/display')
html=BeautifulSoup(res.text,'html.parser')
title=html.find('title')
print(title.text)
