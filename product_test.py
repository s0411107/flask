import json
from urllib.request import Request, urlopen
import random
import time
import threading

SERVER = "localhost:5000"
JSONCONTENTTYPE = "application/json; charset=UTF-8"

def getdata(id):
    data = { "ID" : id }
    req = Request(url = f"http://{SERVER}/api/data",
            data = json.dumps(data).encode("utf-8"),
            headers = {"Content-type": JSONCONTENTTYPE},
            method = "GET")
    with urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    return result

def buyproduct(id , Quantity):
    data = { "ID" : id , "Quantity" : Quantity, "credit_card_id" : str(random.randint(1000000000000000, 9999999999999999))}
    req = Request(url = f"http://{SERVER}/api/buy",
            data = json.dumps(data).encode("utf-8"),
            headers = {"Content-type": JSONCONTENTTYPE},
            method = "POST")
    with urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    return result

def updateproduct(id , Quantity):
    data = { "ID" : id , "Quantity" : Quantity}
    req = Request(url = f"http://{SERVER}/api/update",
            data = json.dumps(data).encode("utf-8"),
            headers = {"Content-type": JSONCONTENTTYPE},
            method = "PUT")
    with urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    return result

if __name__ == "__main__":
    thread1 = threading.Thread(target=getdata, args=(1,))
    thread2 = threading.Thread(target=buyproduct, args=(2, 10))
    thread3 = threading.Thread(target=buyproduct, args=(2, 1000))
    thread4 = threading.Thread(target=updateproduct, args=(2, 100))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()