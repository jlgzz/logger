import threading

periodo= 1.0

def saludo():
    threading.Timer(periodo,saludo).start()
    print("hello world"+","+"be happy")





if  __name__=="__main__":
    saludo()