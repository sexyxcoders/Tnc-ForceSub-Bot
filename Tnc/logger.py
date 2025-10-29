import logging

LOG_FORMAT = "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt="%H:%M:%S"
)

LOG = logging.getLogger("Tnc")
