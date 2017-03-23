# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from resource.index_resource import IndexResource
from injection_configuration import create_injector


class YourApplication(object):
    def __init__(self):
        self.injector = create_injector()

    @staticmethod
    def routes():
        return [
            Route(u'/', IndexResource)
        ]


class Route(object):
    def __init__(self, uri, resource, requires_admin_privileges=False):
        self.uri = uri
        self.resource = resource
        self.requires_admin_privileges = requires_admin_privileges
