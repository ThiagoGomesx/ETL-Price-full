import logging

# Criar configuração básica de logs
logging.basicConfig(
    filename="etl.log",          # arquivo onde os logs vão ficar
    level=logging.INFO,          # nível dos logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

logger = logging.getLogger()