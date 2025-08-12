import logging
import os

def setup_logger():
    """Sets up a structured logger using an absolute path for the log file."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file_path = os.path.join(project_root, 'bot.log')

    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(log_format)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

logger = setup_logger()