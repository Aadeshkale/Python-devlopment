import requests
from bs4 import BeautifulSoup
res=requests.get('https://aadesh.pythonanywhere.com/myapp/display')
html=BeautifulSoup(res.text,'html.parser')
table=html.find('table')
# geting table head
thead=table.find('thead')
td=thead.findAll('td')
s=""
f=open('out.csv','w')
for i in td:
    s+=i.text+','
f.write(s+'\n')
# getting table data
tbody=table.findAll('tbody')
for i in tbody:
    r=i.findAll('td')
    s=""
    for i in r:
        s+=i.text+','
    f.write(s+'\n')
f.close()