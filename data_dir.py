import struct

from field import Field


class DataDir:
    def __init__(self, fmt, data_dir_header_data):
        data_dir_header_values = struct.unpack(fmt, data_dir_header_data)
        self.export_dir_address = data_dir_header_values[0]
        self.export_dir_size = data_dir_header_values[1]
        self.import_dir_address = data_dir_header_values[2]
        self.import_dir_size = data_dir_header_values[3]
        self.resource_dir_address = data_dir_header_values[4]
        self.resource_dir_size = data_dir_header_values[5]
        self.exception_dir_address = data_dir_header_values[6]
        self.exception_dir_size = data_dir_header_values[7]
        self.security_dir_address = data_dir_header_values[8]
        self.security_dir_size = data_dir_header_values[9]
        self.base_relocation_dir_address = data_dir_header_values[10]
        self.base_relocation_dir_size = data_dir_header_values[11]
        self.debug_dir_address = data_dir_header_values[12]
        self.debug_dir_size = data_dir_header_values[13]
        self.copyright_dir_address = data_dir_header_values[14]
        self.copyright_dir_size = data_dir_header_values[15]
        self.cpu_spec_dir_address = data_dir_header_values[16]
        self.cpu_spec_dir_size = data_dir_header_values[17]
        self.TLS_dir_address = data_dir_header_values[18]
        self.TLS_dir_size = data_dir_header_values[19]
        self.config_dir_address = data_dir_header_values[20]
        self.config_dir_size = data_dir_header_values[21]

    def get_data_dir_info(self):
        fields = [
            Field(size=2, ph_address=0, name='Export Dir Address',
                  value=self.export_dir_address),
            Field(size=2, ph_address=0, name='Export Dir Size',
                  value=self.export_dir_size),
            Field(size=2, ph_address=0, name='Import Dir Address',
                  value=self.import_dir_address),
            Field(size=2, ph_address=0, name='Import Dir Size',
                  value=self.import_dir_size),
            Field(size=2, ph_address=0, name='Resource Dir_address',
                  value=self.resource_dir_address),
            Field(size=2, ph_address=0, name='Resource Dir Size',
                  value=self.resource_dir_size),
            Field(size=2, ph_address=0, name='Exception Dir Address',
                  value=self.exception_dir_address),
            Field(size=2, ph_address=0, name='Exception Dir Size',
                  value=self.exception_dir_size),
            Field(size=2, ph_address=0, name='Security Dir Address',
                  value=self.security_dir_address),
            Field(size=2, ph_address=0, name='Security Dir Size',
                  value=self.security_dir_size),
            Field(size=2, ph_address=0, name='Base Relocation Dir Address',
                  value=self.base_relocation_dir_address),
            Field(size=2, ph_address=0, name='Base Relocation Dir Size',
                  value=self.base_relocation_dir_size),
            Field(size=2, ph_address=0, name='Debug Dir Address',
                  value=self.debug_dir_address),
            Field(size=2, ph_address=0, name='Debug Dir Size',
                  value=self.debug_dir_size),
            Field(size=2, ph_address=0, name='Copyright Dir Address',
                  value=self.copyright_dir_address),
            Field(size=2, ph_address=0, name='Copyright Dir Size',
                  value=self.copyright_dir_size),
            Field(size=2, ph_address=0, name='Cpu Dir Address',
                  value=self.cpu_spec_dir_address),
            Field(size=2, ph_address=0, name='Cpu Dir Size',
                  value=self.cpu_spec_dir_size),
            Field(size=2, ph_address=0, name='TLS Dir Address',
                  value=self.TLS_dir_address),
            Field(size=2, ph_address=0, name='TLS Dir Size',
                  value=self.TLS_dir_size),
            Field(size=2, ph_address=0, name='Config Dir Address',
                  value=self.config_dir_address),
            Field(size=2, ph_address=0, name='Config Dir Size',
                  value=self.config_dir_size),
        ]
        return fields
