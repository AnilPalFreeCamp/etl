from abc import ABC
from abc import abstractmethod
from os import path
import os
from parser import utility as util
import glob
import csv
import json
from transformation.numerical_trans import NumericalTransformation, round_of_number
from transformation.date_transformation import DateTransformation, format_date
from transformation.regex_trans import RegexTransformation
from transformation.transform_base import BaseTransform
from transformation.string_transform import StringTransformation


def write_parsed_records(file_name, output):
    print("writing dictionary", output)
    if len(output) == 0:
        return;
    if not path.exists(file_name):
        with open(file_name, 'w') as f:
            fieldnames = output[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\x01')
            writer.writeheader()
            writer.writerows(output)
    else:
        with open(file_name, 'a') as f:
            fieldnames = output[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\x01')
            writer.writerows(output)
    return file_name;


class BaseParser:
    '''
    classdocs
    '''

    def __init__(self, trans_info):
        util.validate_trans_info(trans_info)
        self.trans_info = trans_info
        self.input_folder_path = self.trans_info["trans_meta"]["input_folder_path"]
        if "output_folder_path" in trans_info["trans_meta"]:
            self.output_folder_path = trans_info["trans_meta"]["output_folder_path"]
        self.regex_transform = RegexTransformation()
        self.date_format = self.trans_info["trans_meta"]["date_format"]
        self.numerical_transform = NumericalTransformation()
        self.string_transform = StringTransformation()
        self.date_transform = DateTransformation()

    # self.base_transform = BaseTransform()

    def transform(self, row_dict):
        if "lambda_function" in self.trans_info["trans_info"]:
            lambda_express = self.trans_info["trans_info"]["lambda_function"]["lambda_expression"]
            lambda_express_columns = self.trans_info["trans_info"]["lambda_function"]["consumer_columns"]
            self.perform_lambda_expression(row_dict, lambda_express, lambda_express_columns)
        if "regex_info" in self.trans_info["trans_info"]:
            regex_pattern = self.trans_info["trans_info"]["regex_info"]["regex"]
            regex_columns = self.trans_info["trans_info"]["regex_info"]["consumer_columns"]
            self.perform_regex_validation(row_dict, regex_pattern, regex_columns)
        for key, value in row_dict.items():
            if util.is_float(value):
                value = round_of_number(float(value), 2)
                row_dict[key] = value
                continue
            if util.is_date(value, self.date_format):
                value = format_date(value, self.date_format)
                row_dict[key] = value
                continue
            value = self.string_transform.transform(value)
            row_dict[key] = value
        return row_dict

    def perform_lambda_expression(self, var, lambda_express, columns):
        for key, value in var.items():
            if key in columns:
                value = self.regex_transform.evaluate_lambda_expr(value, lambda_express)
                var[key] = value

    def perform_regex_validation(self, var, pattern, columns):
        for key, value in var.items():
            if key in columns:
                value = self.regex_transform.transform(value, pattern)
                var[key] = value

    def process(self):
        util.validate_path(self.input_folder_path)
        self.parse_dir(self.input_folder_path)

    def parse(self, input_path):
        raise Exception("Not implemented")
