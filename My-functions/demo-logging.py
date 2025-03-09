# demonstrate the logging module

import logging

import traceback

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,  # Set the threshold for this logger
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Different log levels (in increasing order of severity)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Creating a logger with a specific name
logger = logging.getLogger('my_custom_logger')
logger.warning('This is a warning from the custom logger')

# Logging to a file
file_handler = logging.FileHandler('app.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.DEBUG)
file_logger.addHandler(file_handler)
file_logger.info('This message will be written to the app.log file')

# Using try-except with logging
try:
    # Intentional division by zero to demonstrate logging of exceptions
    result = 10 / 0
# Catching all exceptions
except Exception as e:
    logging.exception(f"An error occurred: {e}")  # Will log traceback information
    file_logger.error(f"Error: {e}\n{traceback.format_exc()}")

def setup_logger(logger_name, log_file, level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    
    # Create file handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(level)
    
    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    
    # Create formatter and add to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

# Example usage of the custom logger setup
custom_logger = setup_logger('example_logger', 'example.log')
custom_logger.info('This is an example log message')