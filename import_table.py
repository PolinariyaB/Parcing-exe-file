import struct


class ImportTable:
    def __init__(self, fmt, import_table_data):
        self.fmt = fmt
        self.import_table_data = import_table_data
        self.unpack_data()

    def unpack_data(self):
        import_table_values = struct.unpack(self.fmt, self.import_table_data)
        self.original_first_thunk = import_table_values[0]
        self.time_date_stamp = import_table_values[1]
        self.forwarder_chain = import_table_values[2]
        self.name_rva = import_table_values[3]
        self.first_thunk = import_table_values[4]

    def all_zero(self):
        return (self.original_first_thunk == 0 and
                self.time_date_stamp == 0 and
                self.forwarder_chain == 0 and
                self.name_rva == 0 and
                self.first_thunk == 0)
