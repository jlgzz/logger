import threading
import requests


periodo= 1.0

"""
def printIt(renglon:str="hola"):
    threading.Timer(periodo,printIt).start()
    print(renglon)"""

def get_data(url:str,parametro:str):
    #request object
    r=requests.get(url)

    if r.ok:
        data=r.json()
        #return(data)
        valor=data[parametro]
        return(valor)
    else:
        return(r.status_code)

"""
if  __name__=="__main__":
    get_data()  
"""













