import abc
from generator import  utility as util


class GenBase(abc.ABC):

    @abc.abstractmethod
    def write_file(self, input, file_name, file_mode):
        raise Exception("Not implemented")


class JSon(GenBase):
    def write_file(self, input_d, file_name, file_mode):
        return util.lis_of_map_to_json(input_d, file_name, file_mode)


class CSV(GenBase):
    def write_file(self, input_d, file_name, file_mode):
        return util.lis_of_map_to_csv(input_d, file_name, file_mode)
