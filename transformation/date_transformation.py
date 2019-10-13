from datetime import datetime
from transformation.transform_base import BaseTransform


def format_date(var, req_format):
    date_object = datetime.strptime(var, req_format)
    return date_object


class DateTransformation(BaseTransform):

    def transform(self, var, function=None):
        return format(var, function)
