"""module for app logging"""

import logging
import os

def _get_filename() -> str:
    """get filename for current file"""

    filename = os.path.basename(p=__file__)
    return filename
