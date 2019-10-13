from parser.base_parser import BaseParser
from parser import utility as util
from os import path
import csv
import os
from parser.base_parser import write_parsed_records


class CSVParser(BaseParser):

    def __init__(self, trans_info):
        super().__init__(trans_info)
        self.trans_info = trans_info

    def parse(self, input_path):
        print("processing input path ", input_path)
        util.validate_path(input_path)
        if path.isdir(input_path):
            raise Exception("CSVParser can't parse a folder")
        else:
            return self.parse_file(input_path)

    def parse_file(self, input_path):
        csv_rows = csv.DictReader(open(input_path))
        filename, file_extension = os.path.splitext(input_path)
        output_file_url = self.trans_info["trans_meta"]["output_folder_path"]
        output_file_url = output_file_url if output_file_url + "/" + filename else util.get_output_path(input_path)
        output_list = []
        for row in csv_rows:
            transformed_row = super(CSVParser, self).transform(row)
            output_list.append(transformed_row)
            chunk_size = self.trans_info["trans_meta"]["chunk_size"]
            chunk_size = chunk_size if chunk_size else 1000
            if len(output_list) == int(chunk_size):
                write_parsed_records(output_file_url, output_list)
                output_list.clear()
        write_parsed_records(output_file_url, output_list)
