import pandas as pd
import parser.utility as util
import mysql.connector
import json

sql = "INSERT INTO etl_stats (file_name, stats) VALUES (%s, %s)"


class Load:
    def __init__(self, input_dir):
        util.validate_path(input_dir)
        self.input_dir = input_dir
        self.mysql_conn = mysql.connector.connect(host='localhost', database='demo', user='root',
                                                  password='root', port=3306)

    def calculate_stats(self):
        file_data = pd.read_csv(self.input_dir, sep='\x01')
        stats_dic = file_data.describe().to_dict()
        val = self.input_dir, json.dumps(stats_dic)
        self.mysql_conn.cursor().execute(sql, val)
        self.mysql_conn.commit()
