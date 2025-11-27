from fastapi import FastAPI
import json
import os

app = FastAPI()

# Arquivo de banco simples
DB_FILE = "prices.json"

# Se não existir, cria
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)

@app.get("/prices")
def get_prices():
    with open(DB_FILE, "r") as f:
        data = json.load(f)
    return data

@app.post("/prices")
def add_price(item: dict):
    with open(DB_FILE, "r") as f:
        data = json.load(f)

    item["id"] = len(data) + 1
    data.append(item)

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return item