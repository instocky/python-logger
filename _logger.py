import logging
import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

# Инициализация colorama
init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Back.WHITE
    }

    def format(self, record):
        log_message = super().format(record)
        return f"{self.COLORS.get(record.levelname, '')}{log_message}{Style.RESET_ALL}"

def setup_logger(log_file=None, console_level=logging.INFO, file_level=logging.DEBUG):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Устанавливаем самый низкий уровень для логгера
    
    # Обновленный формат с именем файла и номером строки
    log_format = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'

    # Форматтер для логов
    file_formatter = logging.Formatter(log_format)
    console_formatter = ColoredFormatter(log_format)

    # Обработчик для консоли
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Обработчик для файла (если указан)
    if log_file:
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(file_level)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

# Создаем короткие алиасы для уровней логирования
d = logging.DEBUG
i = logging.INFO
w = logging.WARNING
e = logging.ERROR
c = logging.CRITICAL

# Пример использования:
# logger = setup_logger(log_file='app.log')
# logger.debug('Debug message')
# logger.info('Info message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')