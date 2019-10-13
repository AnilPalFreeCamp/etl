from parser.base_parser import BaseParser
from parser import utility as util
from os import path
import os
import json
from parser.base_parser import write_parsed_records


class JSONParser(BaseParser):

    def __init__(self, trans_info):
        super().__init__(trans_info)
        self.trans_info = trans_info

    def parse(self, input_path):
        util.validate_path(input_path)
        if path.isdir(input_path):
            raise Exception("folder is giving inplace of file")
        else:
            return self.parse_file(input_path)

    def parse_file(self, input_path):
        output_file_url = self.trans_info["trans_meta"]["output_folder_path"]
        filename, file_extension = os.path.splitext(input_path)
        output_file_url = output_file_url if output_file_url + "/" + filename else util.get_output_path(
            input_path)
        output_list = []
        chunk_size = 10000
        if "chunk_size" in self.trans_info["trans_meta"]:
            chunk_size = int(self.trans_info["trans_meta"]["chunk_size"])
        with open(input_path, 'r') as json_file:
            for line in json_file:
                json_row = json.loads(line)
                transformed_row = super(JSONParser, self).transform(json_row)
                output_list.append(transformed_row)
                if len(output_list) == int(chunk_size):
                    write_parsed_records(output_file_url, output_list)
                    output_list.clear()
        write_parsed_records(output_file_url, output_list)
