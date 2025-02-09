import logging


def setup_logger(name: str) -> logging.Logger:
    """Set up logger object.

    Args:
        name (str): logger name

    Returns:
        logging.Logger: logger object.
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
