import json , socket , hashlib
from flask import Flask, jsonify, request
app = Flask(__name__)

# A list of dicts, e.g. { "id": 12, "desc": "Do work" }
def EXE_ID(): 
     time = ""
     global exe_id
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     host = "time-a-g.nist.gov"
     port = 13
     try: # get the time from "time-a-g.nist.gov"
         s.connect((host,port))
         data = s.recv(1024)
         time = str(data , encoding='utf-8')
     except Exception as e:
         print("ERROR!")    
     exe_id = hashlib.sha256(time.encode()).hexdigest() # change the time to hex data
     return exe_id
total = 0

@app.route("/api/data", methods=["GET"])
def get_data():
    with open('product.json') as f:
        json_data = json.load(f) #get data from production json
    data = json.loads(request.data) #save production data to "data"
    ID = data.get("ID")
    product = json_data[ID]
    exe_id = EXE_ID()
    return jsonify({"product": product , "exeid" : exe_id})

@app.route("/api/buy", methods=["POST"])
def buy_product():
    amount = 0
    sum = 0
    with open('product.json') as f:
        json_data = json.load(f)
    data = json.loads(request.data)
    ID = data.get("ID")
    product = json_data[ID]
    ID1 = product.get("id")
    Price = product.get("Price")
    CardID = data.get("credit_card_id")
    quantity = product.get("Quantity")
    dataquantity = data.get("Quantity")
    exe_id = EXE_ID()
    if type(quantity) != int or quantity < 0:
        return jsonify({"HTTP Error 400": " BAD REQUEST"}) #when the data from production is not correct, send the error message
    elif quantity  >= dataquantity:
        amount = Price * dataquantity
        sum = quantity - dataquantity
        if [ID1] == [ID + 1]:
                json_data[ID]["Quantity"] = sum
        with open('product.json', 'r+') as f:
             json.dump(json_data , f , ensure_ascii=False)
        return jsonify({"status": "success", "credit card id" : CardID , "amount": amount, "exeid" : exe_id})
    else:
        return jsonify({"status": "failure (insufficient quantity)"})

@app.route("/api/update", methods=["PUT"])
def update_product():
    sum = 0
    data = json.loads(request.data)
    with open('product.json') as f:
        json_data = json.load(f)
    data = json.loads(request.data)
    ID = data.get("ID")
    product = json_data[ID]
    ID1 = product.get("id")
    quantity = product.get("Quantity")
    dataquantity = data.get("Quantity")
    sum = quantity + dataquantity 
    exe_id = EXE_ID()
    if [ID1] == [ID + 1]:
            json_data[ID]["Quantity"] = sum #save the updata data to product.json
    with open('product.json', 'r+') as f:
             json.dump(json_data , f , ensure_ascii=False)
    return jsonify({"status": "success", "exeid" : exe_id})

if __name__ == "__main__":
    app.run()
