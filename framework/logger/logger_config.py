import os
import logging


class LoggerConfig:
    LOGS_DIR_NAME = "logs"
    LOGGER_NAME = "Logger"
    LOGS_FILE_NAME = os.path.join(LOGS_DIR_NAME, "test.log")
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    FORMAT = "[%(asctime)s | %(levelname)s] %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    encoding = 'utf-8'
