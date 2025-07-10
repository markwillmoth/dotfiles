import logging
import os
from logging.handlers import RotatingFileHandler


class RelativePathFormatter(logging.Formatter):
    def format(self, record):
        record.relpath = os.path.relpath(record.pathname, start=os.getcwd())
        return super().format(record)


logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

_file_handler = RotatingFileHandler(
    "/tmp/hyprcmd.log", maxBytes=5 * 1024 * 1024, backupCount=3
)

_formatter = RelativePathFormatter(
    "%(asctime)s %(levelname)s [%(relpath)s:%(lineno)d] %(message)s"
)
_file_handler.setFormatter(_formatter)

if not logger.handlers:
    logger.addHandler(_file_handler)
