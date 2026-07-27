import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

class logger:
    def __init__(self, name: str = "Phoenix", level: int = logging.INFO):
        os.makedirs(LOG_DIR, exist_ok=True)
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)
        if not self._logger.handlers:
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
            file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)

            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            stream_handler.setFormatter(formatter)
            self._logger.addHandler(stream_handler)

    def get_logger(self):
        return self._logger

if __name__ == "__main__":
    log = logger().get_logger()
    log.info("Logger initialized successfully.")
    log.debug("This is a debug message.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")
    log.critical("This is a critical message.")