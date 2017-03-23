# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import sys
import logging
from flask_injector import FlaskInjector
from server import Server
from your_application import YourApplication


def create_log_handler():
    from configuration import logging_configuration

    formatter = logging.Formatter(logging_configuration[u'pattern'])
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    handler.setLevel(logging_configuration[u'level'])
    return handler


log_handler = create_log_handler()
root_logger = logging.getLogger()
del root_logger.handlers[:]
root_logger.setLevel(log_handler.level)
root_logger.addHandler(log_handler)

application = YourApplication()
server = Server(application)

FlaskInjector(app=server.flask, injector=application.injector)
