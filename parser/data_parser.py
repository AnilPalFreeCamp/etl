import os

from parser.csv_parser import CSVParser
from parser.json_parser import JSONParser
from parser.base_parser import BaseParser
import json

trans_info = {}
with open(os.path.join(os.getcwd(), "resource") + "/transformation_info", 'r') as f:
    trans_info = json.load(f)
csv_parser = CSVParser(trans_info)
json_parser = JSONParser(trans_info)


def parse_dir(input_path):
    for file_name in os.listdir(input_path):
        print(" found", file_name)
        path_process = os.path.join(input_path, file_name)
        if os.path.isdir(path_process):
            parse_dir(path_process)
            continue
        filename, file_extension = os.path.splitext(path_process)
        print(filename, file_extension)
        if file_extension == ".csv":
            csv_parser.parse(path_process)
        else:
            json_parser.parse(path_process)


def execute():
    parse_dir(trans_info["trans_meta"]["input_folder_path"])
