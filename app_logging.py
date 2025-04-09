"""module for app logging"""

import logging
import os


file_format = "[%(asctime)s]: [%(name)s]: [%(filename)s]: [%(levelname)s]: [%(message)s]"
stream_format = "[%(asctime)s]: [%(funcName)s]: [%(lineno)s]: [%(levelname)s]: [%(message)s]"


def _get_filename() -> str:
    """get filename for current file"""

    filename = os.path.basename(p=__file__)
    return filename


