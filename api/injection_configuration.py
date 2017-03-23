# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import logging

from injector import singleton, Module, Injector

from api.infrastructure.bus import CommandBus, QueryBus, CommandHandlers, QueryHandlers
from api.infrastructure.handlers import CommandHandler, QueryHandler
from utils import find_implementations_of

logger = logging.getLogger(__name__)


def create_injector():
    return Injector([InjectionModule()])


class InjectionModule(Module):
    def configure(self, binder):
        self._configure_commands(binder)
        self._configure_queries(binder)

    def _configure_commands(self, binder):
        command_handlers = self._implementations_of(CommandHandler)
        binder.multibind(CommandHandlers, to=command_handlers, scope=singleton)
        binder.bind(CommandBus, scope=singleton)

    def _configure_queries(self, binder):
        query_handlers = self._implementations_of(QueryHandler)
        binder.multibind(QueryHandlers, to=query_handlers, scope=singleton)
        binder.bind(QueryBus, scope=singleton)

    def _implementations_of(self, clazz):
        query_handlers = []
        implementations = find_implementations_of(clazz)
        for implementation in implementations:
            logger.debug(u'Found implementation for %s => %s', clazz.__name__, implementation.__name__)
            query_handlers.append(self.__injector__.get(implementation))
        return query_handlers
