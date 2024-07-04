import os  # to create a folder in current working directory for logs
import sys  # sys is a built-in module in python which provides access to some variables used or maintained by the interpreter at runtime.
import pandas as pd  # to read the csv file
import numpy as np  # for mathematical operations
from sklearn.model_selection import train_test_split  # to split the data into train and test

# Add the src directory to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(src_dir)

from src.exception import CustomException  # to handle exceptions
from src.logger import logging  # to log all information in file that can be used to trace the errors in the code
from dataclasses import dataclass  # to create a dataclass for the class variables

@dataclass
class DataIngestionConfig:  # to create a dataclass for the class variables
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv(r'notebook\data\stud.csv')  # Fixed the SyntaxWarning
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
