import multiprocessing
import requests
import concurrent.futures
def downloadFile(url,name):
    print(f"Started Downloading {name}.jpg")
    response=requests.get(url)
    open(f"Files3/File{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}.jpg")
if __name__=="__main__":
    url="https://picsum.photos/2000/3000"
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[url for i in range(60)]
        l2=[i for i in range(60)]
        results=executor.map(downloadFile,l1,l2)
        for r in results:
            print(r)