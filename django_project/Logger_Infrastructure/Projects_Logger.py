import logging
from datetime import datetime
from pathlib import Path
from colorlog import ColoredFormatter


class ProjectsLogging:
    def __init__(self, project_name, path=None, file_name=None):
        self.path = path
        self.file_name = file_name
        self.project_name = project_name
        now = datetime.now()
        self.dt_string = now.strftime("%d_%m_%Y %H_%M_%S")
        if not self.path:
            self.path = 'C:/' + 'Python Logs/' + self.project_name + '/' + self.dt_string
        else:
            self.path = self.path
        Path(self.path).mkdir(parents=True, exist_ok=True)

    def project_logging(self, t_f=False):
        logger = logging.getLogger(__name__)
        stream = logging.StreamHandler()

        LOG_LEVEL = logging.DEBUG
        logger.setLevel(LOG_LEVEL)
        # logging.root.setLevel(LOG_LEVEL)

        if t_f:
            LOGFORMAT_CONSOLE = "%(log_color)s%(asctime)s | %(levelname)-8s%(reset)s %(log_color)s | " \
                                "%(log_color)s%(message)s%(reset)s"
            LOGFORMAT_FILE = "%(asctime)s | %(levelname)-8s:%(name)s | %(message)s"
        else:
            LOGFORMAT_CONSOLE = "%(log_color)s%(asctime)s | %(levelname)-8s%(reset)s %(log_color)s | " \
                                "%(log_color)s%(message)s%(reset)s"
            LOGFORMAT_FILE = "%(asctime)s | %(levelname)-8s | %(message)s"

        formatter_file = logging.Formatter(LOGFORMAT_FILE)
        formatter_console = ColoredFormatter(LOGFORMAT_CONSOLE)
        if not self.file_name:
            file_handler = logging.FileHandler(self.path + '/' + self.dt_string + '.log', mode='a')
        else:
            file_handler = logging.FileHandler(
                self.path + '/' + self.file_name + '.log', mode='a')
        # file_handler = logging.FileHandler('c:/tmp/test.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter_file)

        stream.setLevel(LOG_LEVEL)
        stream.setFormatter(formatter_console)

        logger.setLevel(LOG_LEVEL)
        logger.addHandler(file_handler)
        logger.addHandler(stream)

        return logger
