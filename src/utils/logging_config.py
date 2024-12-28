import logging


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("../bot.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)
