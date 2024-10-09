from _logger import setup_logger, d, i, w, e, c

# Настройка логгера
logger = setup_logger(log_file='app.log', console_level=e, file_level=d)

# Использование
logger.debug('Это отладочное сообщение')
logger.info('Это информационное сообщение')
logger.warning('Это предупреждение')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')

# Использование с короткими алиасами
logger.log(w, 'Отладочное сообщение с использованием алиаса')
logger.log(i, 'Информационное сообщение с использованием алиаса')