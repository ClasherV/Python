from bs4 import BeautifulSoup
import requests
url="https://www.pinterest.com/orginalsaber/ada-wong-resident-evil/"
r=requests.get(url)
print(r.text)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())