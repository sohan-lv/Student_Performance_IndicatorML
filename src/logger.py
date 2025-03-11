import logging
import os
from datetime import datetime

# Create a log file with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(os.getcwd(), LOG_FILE)
os.makedirs(LOG_FILE_PATH, exist_ok=True)

# Full path for the log file
logs_path= os.path.join(LOG_FILE_PATH, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)