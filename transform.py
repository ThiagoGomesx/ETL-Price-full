import pandas as pd
from logger import logger

def transform_prices(df: pd.DataFrame):
    logger.info("Iniciando transformação dos dados")

    df = df.rename(columns={
        "title": "product_name",
        "price": "price_original"
    })

    df["price_adjusted"] = df["price_original"] * 1.10

    logger.info("Transformação concluída")

    return df