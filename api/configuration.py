# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import logging

logging_configuration = {
    u'level': logging.DEBUG,
    u'pattern': u'[%(asctime)s] [%(name)s] %(levelname)s | %(message)s'
}

http_configuration = {
    u'number_of_retries': 5,
    u'maximum_retry_delay_in_seconds': 32
}
