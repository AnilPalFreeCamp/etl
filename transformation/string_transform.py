import re
from transformation.transform_base import BaseTransform


def remove_space_from_middle(var):
    if not var:
        return "NA"
    return re.sub("\s+", " ", var).strip()


def remove_non_ascii(var):
    if not var:
        return "NA"
    return re.sub(r'[^\x00-\x7F]+', '', var)


class StringTransformation(BaseTransform):

    def transform(self, var, function=None):
        var = remove_space_from_middle(var)
        var = remove_non_ascii(var)
        return var
