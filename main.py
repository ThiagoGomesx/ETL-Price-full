from extract import extract_prices
from transform import transform_prices
from load import load_to_sql
from logger import logger

def run_etl():
    logger.info("=== Iniciando execução completa do ETL ===")

    df_extract = extract_prices()
    df_transform = transform_prices(df_extract)
    load_to_sql(df_transform)

    logger.info("=== ETL finalizado com sucesso ===")
    print("✔ ETL concluído com sucesso!")

if __name__ == "__main__":
    run_etl()