import requests
url="https://www.pinterest.com/orginalsaber/ada-wong-resident-evil/"
data={
    "title": 'foo',
    "body": 'bar',
    "userId": 1
}
headers={
    'Content-type': 'application/json; charset=UTF-8'
}
response=requests.post(url,headers=headers,json=data)
print(response.text)