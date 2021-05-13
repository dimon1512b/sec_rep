import logging_configuration
import logging.config
logging.config.dictConfig(logging_configuration.LOGGING)
logger = logging.getLogger('logger_conf_2')

logger.info('info from LOG___2')