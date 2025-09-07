import logging
import logging.handlers
import sys
import os
from framework.logger.logger_config import LoggerConfig


class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    _formatter = logging.Formatter(fmt=LoggerConfig.FORMAT, datefmt=LoggerConfig.DATETIME_FORMAT)
    _logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    _logger.setLevel(LoggerConfig.LOGS_LEVEL)
    _handler1 = logging.handlers.RotatingFileHandler(
        LoggerConfig.LOGS_FILE_NAME,
        maxBytes=LoggerConfig.MAX_BYTES,
        backupCount=LoggerConfig.BACKUP_COUNT
    )
    _handler2 = logging.StreamHandler(sys.stdout)
    _handler1.setFormatter(_formatter)
    _handler2.setFormatter(_formatter)
    _logger.addHandler(_handler1)
    _logger.addHandler(_handler2)

    @staticmethod
    def set_level(level: str) -> None:
        """Позволяет динамически менять уровень логирования."""
        Logger._logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        """Записывает информационное сообщение."""
        Logger._logger.info(msg=message)

    @staticmethod
    def debug(message: str) -> None:
        """Записывает отладочное сообщение."""
        Logger._logger.debug(msg=message)

    @staticmethod
    def warning(message: str) -> None:
        """Записывает предупреждение."""
        Logger._logger.warning(msg=message)

    @staticmethod
    def error(message: str) -> None:
        """Записывает сообщение об ошибке."""
        Logger._logger.error(msg=message)
