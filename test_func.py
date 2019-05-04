import logging
from config import LoggingConfiguration

# first, apply logging config
LoggingConfiguration()

logger = logging.getLogger('test')

a = 3
b = 6
logger.info('a is {a}, b is b {b}'.format(a=a, b=b))
c = a + b
logger.info('c is {c}'.format(c=c))
