import requests
import pandas as pd
from logger import logger

def extract_prices():
    logger.info("Iniciando extração de preços da API")

    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    if response.status_code != 200:
        logger.error(f"Erro na API: {response.status_code}")
        raise Exception("Falha na extração")

    data = response.json()
    df = pd.DataFrame(data)[["id", "title", "price"]]

    logger.info(f"Extração concluída: {len(df)} registros")

    return df