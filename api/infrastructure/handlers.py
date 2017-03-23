# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from abc import ABCMeta, abstractmethod, abstractproperty


class MessageHandler(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def message_type(self):
        raise AttributeError

    @abstractmethod
    def execute(self, query):
        raise NotImplementedError


class CommandHandler(MessageHandler):
    __metaclass__ = ABCMeta


class QueryHandler(MessageHandler):
    __metaclass__ = ABCMeta
