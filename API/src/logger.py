import logging
import sys
from src.utils.singleton import Singleton

class Logger(metaclass=Singleton):
    
    def __init__(self):
        self.__setup_logger()

    def __setup_logger(self):
        
        log_level = logging.INFO

        self.logger = logging.getLogger('logger')

        self.logger.setLevel(log_level)
        self.logger.propagate = False

        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)

        log_formatter = f'[%(levelname)s] %(asctime)s; %(message)s'
        formatter = logging.Formatter(log_formatter)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, *args, **kwargs):
        message = self._format_log_info(*args, **kwargs)
        self.logger.info(message)

    def warning(self, *args, **kwargs):
        message = self._format_log_info(*args, **kwargs)
        self.logger.warning(message)

    def error(self, *args, **kwargs):
        message = self._format_log_info(*args, **kwargs)
        self.logger.error(message)

    def _format_log_info(self, *args, **kwargs):
        self.message_info = args[0]
        self.log_info = kwargs.get('log_info', {})
        self.id_container = self.log_info.get('id_container')
        self.id_operation = self.log_info.get('id_operation')
        self.username = self.log_info.get('username')

        log_message = f'{self.message_info}'
        return log_message
