import datetime
from os import path
import os
from datetime import datetime

def validate_trans_info(trans_info):
    if not trans_info:
        raise Exception("transformation is not null/Empty")
    if not trans_info["trans_meta"]:
        raise Exception("transformation meta info is missing")
    if not trans_info["trans_meta"]["input_folder_path"]:
        raise Exception("transformation meta info input path is missing")


def validate_path(input_path):
    if not input_path:
        raise Exception("input_path is empty")
    if not path.exists(input_path):
        raise Exception("input path doesn't exists")
    return input_path


def is_empty(input_path):
    if not input_path:
        raise Exception("string is empty")


def get_output_path(file_name):
    if path.isfile(file_name):
        output_name = os.path.splitext(os.path.basename(file_name))[0]
        dir_path = os.path.dirname(os.path.realpath(file_name))
        dir_path = dir_path + "/parsed_output"
        if not path.exists(dir_path):
            os.mkdir(dir_path)
        return dir_path + "/" + output_name + ".txt";


def is_float(val):
    try:
        val = float(val)
    except:
        return False
    return True


def is_date(val, date_format):
    try:
        val = datetime.strptime(val, date_format)
    except:
        return False
    return True
