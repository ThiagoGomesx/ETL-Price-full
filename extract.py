import requests
import pandas as pd

def extract_prices():
    url = "http://127.0.0.1:8000/prices"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # transforma a resposta da API em DataFrame
    df = pd.DataFrame(data)

    return df