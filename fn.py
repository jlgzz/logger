
import requests
import time
import csv

periodo= 1.0

"""
def addToCsv(dato):
    with open('dataLog.csv',"a",newline="") as logFile:
        writer=csv.writer(logFile)
        writer.writerow(dato)

"""
def get_data(url:str,key:str):
    r=requests.get(url) #request object
    if r.ok:
        data=r.json() #json to dict
        valor=data[key]
        return(valor,r.ok)
    else:
        return(r.status_code)

def printIt(dato,status:bool):
    while status:
        time.sleep(periodo)

        print(dato)

"""
if  __name__=="__main__":
    get_data()  
"""













