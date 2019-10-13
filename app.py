from generator.data_gen_execute import gen_data
from parser.base_parser import write_parsed_records
from parser.base_parser import BaseParser
import json
from parser.data_parser import execute
import mysql.connector
from load.load_data import Load

import pandas as pd


load = Load('/home/anil/PycharmProjects/etl/generate_data/2019-10-13/parsed')
load.calculate_stats()
"""
print(input_file)
print(input_file.head())
print(input_file.describe().to_dict())
print(json.dumps(input_file.describe().to_dict()))
cnx = mysql.connector.connect(host='localhost', database='demo', user='root', password='root', port=3306)
print(cnx)"""

"""if __name__ == "__main__":
    execute()
    #gen_data() """
