import threading
periodo= 1.0

def saludo():
    threading.Timer(periodo,saludo).start()
    print("Hola mundo"+","+"be happy")





if  __name__=="__main__":
    saludo()