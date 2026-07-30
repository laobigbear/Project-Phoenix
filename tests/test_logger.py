from src.core.logger import get_logger
def test_logger_initialization():
    logger = get_logger()
    assert logger is not None
    assert logger.name == "Phoenix"
    assert logger.level == 20  # logging.INFO level
def test_logger_handlers():
    logger = get_logger()
    assert len(logger.handlers) == 2  # FileHandler and StreamHandler
def test_logger_format():
    logger = get_logger()
    formatter = logger.handlers[0].formatter  # Assuming the first handler is FileHandler
    assert formatter._fmt == "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
def test_logger_stream_handler_level():
    logger = get_logger()
    stream_handler = logger.handlers[1]  # Assuming the second handler is StreamHandler
    assert stream_handler.level == 10  # logging.DEBUG level
def test_logger_file_handler_encoding():
    logger = get_logger()
    file_handler = logger.handlers[0]  # Assuming the first handler is FileHandler
    assert file_handler.encoding == "utf-8"