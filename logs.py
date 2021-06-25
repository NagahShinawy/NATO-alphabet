"""
created by Nagaj at 13/06/2021
"""
import logging
from logging import handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
format_ = logging.Formatter(
    "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
    datefmt="%d/%b/%Y %H:%M:%S",
)

ch = logging.StreamHandler()
ch.setFormatter(format_)
logger.addHandler(ch)

fh = handlers.RotatingFileHandler("logs.log", maxBytes=(1048576 * 5), backupCount=7)
fh.setFormatter(format_)
logger.addHandler(fh)
