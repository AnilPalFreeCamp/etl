from transformation.transform_base import BaseTransform
import re


class RegexTransformation(BaseTransform):

    def transform(self, var, function=None):
        pattern = re.compile(function)
        if not re.match(var):
            raise Exception("Regex validation field on column value " + var)

    def evaluate_lambda_expr(self, var, expr):
        func = lambda x: eval(expr)
        return func(self)
