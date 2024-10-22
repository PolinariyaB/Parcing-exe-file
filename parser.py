import argparse
from typing import Tuple, Any

from export_table import ExportTable
from header_info import HeaderInfo


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Header Info Parser')
        self.parser.add_argument('header_type',
                                 choices=['dos', 'coff', 'pe',
                                          'dir', 'section', 'ex','im'],
                                 help='Type of header')
        self.parser.add_argument('-num', type=int, help='Number of section')
        self.args = vars(self.parser.parse_args())

    def parse_arguments(self) -> tuple[str, Any]:
        header_type = str(self.args["header_type"])
        num = self.args["num"]
        return header_type, num
