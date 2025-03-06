import multiprocessing
import requests
def downloadFile(url,name):
    response=requests.get(url)
    open(f"Files1/File{name}.jpg","wb").write(response.content)
url="https://picsum.photos/2000/3000"
for i in range(5):
    downloadFile(url,i)