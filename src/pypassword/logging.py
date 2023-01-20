import logging


default_handler = logging.StreamHandler()
default_handler.setFormatter(
    logging.Formatter('%(asctime)s %(module)s.%(funcName)s[%(lineno)s] %(levelname)s: %(msg)s')
)

def create_logger() -> logging.Logger:
    """Get the app logger and configure it.

    Logger name is pypass
    
    :returns: the configured app logger
    """
    logger = logging.getLogger('pypass')
    logger.addHandler(default_handler)
    return logger
