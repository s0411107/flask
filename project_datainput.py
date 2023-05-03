# File: logging_env.py
import json
if __name__ == "__main__":
    data = [{"id": 1, "Product": "Apple", "Price": 10, "Quantity": 100}, 
    {"id": 2, "Product": "Orange", "Price": 9, "Quantity": 120},
    {"id": 3, "Product": "Strawberry", "Price": 20, "Quantity": 160},
    {"id": 4, "Product": "Grapefruit", "Price": 13, "Quantity": 10},
    {"id": 5, "Product": "Pineapple", "Price": 22, "Quantity": 130},
    {"id": 6, "Product": "Papaya", "Price": 16, "Quantity": 50},
    {"id": 7, "Product": "Lychee", "Price": 21, "Quantity": 20},
    {"id": 8, "Product": "Banana", "Price": 7, "Quantity": 46},
    {"id": 9, "Product": "Wampi", "Price": 24, "Quantity": 95},
    {"id": 10, "Product": "Fig", "Price": 11, "Quantity": 41}]
    dict_1 = json.dumps(data)
    filename = 'product.json'
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)
