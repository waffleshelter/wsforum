import logging

# Logger config
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Uvicorn logger config
uvicorn_logger = logging.getLogger("uvicorn.error")
uvicorn_logger.setLevel(logging.CRITICAL)