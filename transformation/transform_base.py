from abc import ABC
import abc


class BaseTransform(ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def transform(self, var, function=None):
        raise ValueError('Not implemented')

