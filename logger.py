import logging

logging.basicConfig(
    filename='app.log',              # Log file name
    level=logging.INFO,              # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def logCreation(message):
  logging.info(message)