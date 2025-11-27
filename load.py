import pandas as pd
from sqlalchemy import create_engine
from logger import logger

def load_to_sql(df: pd.DataFrame):
    logger.info("Iniciando carga para o banco SQLite")

    engine = create_engine("sqlite:///database.db")
    df.to_sql("prices", engine, if_exists="replace", index=False)

    logger.info("Carga concluída com sucesso: tabela 'prices' atualizada")