import datetime
import logging
from uvicorn.config import LOGGING_CONFIG


def init_logger():
    logger_format = "[%(asctime)s] [%(levelname)s] [%(message)s]"
    logging.Formatter.formatTime = (lambda self, record, datefmt=None:
                                    datetime.datetime.fromtimestamp(record.created)
                                    .isoformat(timespec="seconds"))

    LOGGING_CONFIG["formatters"]["default"]["fmt"] = logger_format
    LOGGING_CONFIG["formatters"]["access"]["fmt"] = logger_format
