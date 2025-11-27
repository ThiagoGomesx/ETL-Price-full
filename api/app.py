from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI(title="API do Projeto ETL")

# =============================================
# 1) Rota simples para testar
# =============================================
@app.get("/")
def home():
    return {"message": "API funcionando!"}

# =============================================
# 2) Rota para listar os preços armazenados
# =============================================
@app.get("/prices")
def get_prices():
    conn = sqlite3.connect("database/prices.db")
    df = pd.read_sql_query("SELECT * FROM prices", conn)
    conn.close()
    return df.to_dict(orient="records")