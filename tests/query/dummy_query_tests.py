# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from unittest import TestCase

from nose.tools import *

from api.query.dummy_query import *


class DummyQueryTestCase(TestCase):
    def test_a_message_is_returned(self):
        handler = DummyQueryHandler()

        result = handler.execute(DummyQuery())

        assert_equals(u'The first query: this is so cool', result)
