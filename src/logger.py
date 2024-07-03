
import logging # to log all information in file that can be use to trace the errors in the code
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # to create a log file with current date and time as name
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # to create a logs folder in current working directory
os.makedirs(logs_path,exist_ok=True) 

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)  
