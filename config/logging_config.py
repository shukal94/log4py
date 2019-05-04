import logging.config
import os
import yaml


class LoggingConfiguration:

    def __init__(self):
        # apply configuration from logging.cfg
        self.apply_configuration()

    @staticmethod
    def apply_configuration():
        path = os.getcwd()
        config = yaml.load(open(path + '/config/logging.cfg', 'r'))
        logging.config.dictConfig(config)
