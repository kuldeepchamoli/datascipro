import os 
import sys
import logging

# Logging format string (corrected 'module' key)
logging_str = "[%(asctime)s:%(levelname)s: %(module)s: %(message)s]"

# Directory and file for logs
log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")

# Create log directory if not exists
os.makedirs(log_dir, exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),     # Save to file
        logging.StreamHandler(sys.stdout)      # Also output to terminal
    ]
)

# Create logger instance
logger = logging.getLogger("datasciprologger")
