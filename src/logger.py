import logging
from src.config import LOG_FILE

def get_logger(name: str="Phoenix", level:int=logging.INFO)->logging.Logger:
    _logger = logging.getLogger(name)
    _logger.setLevel(level)
    if not _logger.handlers:
        formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(formatter)
        _logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        _logger.addHandler(stream_handler)

    return _logger