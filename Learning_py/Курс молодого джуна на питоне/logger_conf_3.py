import logging_configuration
import logging.config
logging.config.dictConfig(logging_configuration.LOGGING)
logger = logging.getLogger('logger_conf_3')

logger.info('info from LOG___3')