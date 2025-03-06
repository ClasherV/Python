import multiprocessing
import requests
def downloadFile(url,name):
    print(f"Started Downloading {name}.jpg")
    response=requests.get(url)
    open(f"Files2/File{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading {name}.jpg")
if __name__=="__main__":
    url="https://picsum.photos/2000/3000"
    pros=[]
    for i in range(5):
        p=multiprocessing.Process(target=downloadFile,args=[url,i])
        p.start()
        pros.append(p)
    for p in pros:
        p.join()