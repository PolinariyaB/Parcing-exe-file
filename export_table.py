import struct


class ExportTable:
    def __init__(self, fmt, data):
        fields = struct.unpack(fmt, data)
        self.export_flags = fields[0]
        self.time_date_stamp = fields[1]
        self.major_version = fields[2]
        self.minor_version = fields[3]
        self.name_rva = fields[4]
        self.ordinal_base = fields[5]
        self.address_table_entries = fields[6]
        self.number_of_name_pointers = fields[7]
        self.export_address_table_rva = fields[8]
        self.name_pointer_rva = fields[9]
        self.ordinal_table_rva = fields[10]
