import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
file = logging.FileHandler("app.log")

console.setLevel(logging.DEBUG)
file.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(levelname)s: %(message)s'
)

console.setFormatter(formatter)
file.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file)

logging.debug("This is a debug message")
logging.info("This is an information message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")