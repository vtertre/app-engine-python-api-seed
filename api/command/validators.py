# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from abc import ABCMeta, abstractmethod
from functools import wraps


class CommandValidator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self, command):
        raise NotImplementedError


class ValidateBeforeWith(object):
    def __init__(self, validator):
        self.validator = validator

    def __call__(self, function):
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            command = args[1]
            violations = self.validator.validate(command)
            if len(violations) > 0:
                raise ValidationError(violations)
            return function(*args, **kwargs)
        return wrapped_function


class ValidationError(RuntimeError):
    status_code = 400

    def __init__(self, messages):
        self.messages = messages
