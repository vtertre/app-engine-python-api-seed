# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from unittest import TestCase

from abc import ABCMeta, abstractmethod
from api.utils import *
from nose.tools import *


class GlobalFunctionsTestCase(TestCase):
    def test_searches_all_the_concrete_implementations_of_a_class(self):
        assert_list_equal([B, D], find_implementations_of(A))


class A(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def do(self):
        pass


class B(A):
    def do(self):
        pass


class C(A):
    __metaclass__ = ABCMeta


class D(C):
    def do(self):
        pass
