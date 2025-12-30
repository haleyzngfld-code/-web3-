from colorlog import ColoredFormatter
import colorlog


def init_logger():
    handler = colorlog.StreamHandler()

    formatter = ColoredFormatter(
        "%(asctime)s %(log_color)s %(levelname)s : %(name)s : %(message)s",
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    handler.setFormatter(formatter)
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel('INFO')
    return logger
