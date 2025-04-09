"""module for app logging"""

import logging
import os


file_format = "[%(asctime)s]: [%(name)s]: [%(filename)s]: [%(levelname)s]: [%(message)s]"
stream_format = "[%(asctime)s]: [%(funcName)s]: [%(lineno)s]: [%(levelname)s]: [%(message)s]"


def _get_filename() -> str:
    """get filename for current file"""

    filename = os.path.basename(p=__file__)
    return filename


def init_logging() -> logging.Logger:
    """logging function"""

    file_log_formatter = logging.Formatter(fmt=file_format)
    stream_log_formatter = logging.Formatter(fmt=stream_format)
    logger = logging.getLogger(name=_get_filename().replace('.py',''))
    file_handler = logging.FileHandler(filename=_get_filename().replace('.py', '.log'))
    stream_handler = logging.StreamHandler()

    logger.addHandler(hdlr=file_handler)
    logger.addHandler(hdlr=stream_handler)

    file_handler.setFormatter(fmt=file_log_formatter)
    stream_handler.setFormatter(fmt=stream_log_formatter)
    
    
    