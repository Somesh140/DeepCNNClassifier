from deepClassifier.config import ConfigurationManager
from deepClassifier.components import DataIngestion
from deepClassifier import logger

STAGE_NAME = "Data Ingestion stage"

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()


if __name__=="__main__":
    try:
        logger.info(f"{'>>'*20} Stage : {STAGE_NAME} started {'<<'*20}")
        main()
        logger.info(f"{'>>'*20} Stage : {STAGE_NAME} completed {'<<'*20} \n\nx=========x\n")
    except Exception as e:
        logger.exception(e)
        raise e