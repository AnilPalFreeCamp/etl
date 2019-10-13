import string
from transformation.transform_base import BaseTransform


def round_of_number(var, precision):
    return round(var, precision)


class NumericalTransformation(BaseTransform):

    def transform(self, var, function=None):
        return round_of_number(var, function)
