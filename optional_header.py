import struct

from dos_header import DOSHeader
from field import Field


class OptionalHeader:
    def __init__(self, fmt, optional_header_data):
        optional_header_values = struct.unpack(fmt, optional_header_data)

        self.magic = optional_header_values[0]
        self.major_linker_version = optional_header_values[1]
        self.minor_linker_version = optional_header_values[2]
        self.size_of_code = optional_header_values[3]
        self.size_of_initialized_data = optional_header_values[4]
        self.size_of_uninitialized_data = optional_header_values[5]
        self.address_of_entry_point = optional_header_values[6]
        self.base_of_code = optional_header_values[7]
        self.base_of_data = optional_header_values[8]
        self.image_base = optional_header_values[9]
        self.section_alignment = optional_header_values[10]
        self.file_alignment = optional_header_values[11]
        self.major_operating_system_version = optional_header_values[12]
        self.minor_operating_system_version = optional_header_values[13]
        self.major_image_version = optional_header_values[14]
        self.minor_image_version = optional_header_values[15]
        self.major_subsystem_version = optional_header_values[16]
        self.minor_subsystem_version = optional_header_values[17]
        self.image_size = optional_header_values[19]
        self.header_size = optional_header_values[20]
        self.check_sum = optional_header_values[22]
        self.subsystem = optional_header_values[22]
        self.dll_flags = optional_header_values[23]
        self.stack_reserve_size = optional_header_values[24]
        self.stack_commit_size = optional_header_values[25]
        self.heap_reserve_size = optional_header_values[26]
        self.heap_comitSize = optional_header_values[27]
        self.loader_flags = optional_header_values[28]
        self.data_dir_size = optional_header_values[29]

    def get_optional_header_info(self):
        fields = [
            Field(size=2, ph_address=0, name='Magic',
                  value=self.magic),
            Field(size=1, ph_address=0, name='Major Linker Version',
                  value=self.major_linker_version),
            Field(size=1, ph_address=0, name='Minor Linker Version',
                  value=self.minor_linker_version),
            Field(size=4, ph_address=0, name='Size of Code',
                  value=self.size_of_code),
            Field(size=4, ph_address=0, name='Size of Initialized Data',
                  value=self.size_of_initialized_data),
            Field(size=4, ph_address=0, name='Size of Uninitialized Data',
                  value=self.size_of_uninitialized_data),
            Field(size=4, ph_address=0, name='Address of entry point',
                  value=self.address_of_entry_point),
            Field(size=4, ph_address=0, name='Base of Code',
                  value=self.base_of_code),
            Field(size=4, ph_address=0, name='Base of Data',
                  value=self.base_of_data),
            Field(size=4, ph_address=0, name='Image base',
                  value=self.image_base),
            Field(size=4, ph_address=0, name='Section Alignment',
                  value=self.section_alignment),
            Field(size=2, ph_address=0, name='File Alignment',
                  value=self.file_alignment),
            Field(size=2, ph_address=0, name='Major Operating System Version',
                  value=self.major_operating_system_version),
            Field(size=2, ph_address=0, name='Minor Operating System Version',
                  value=self.minor_operating_system_version),
            Field(size=2, ph_address=0, name='Major Image Version',
                  value=self.major_image_version),
            Field(size=2, ph_address=0, name='Minor Image Version',
                  value=self.minor_image_version),
            Field(size=2, ph_address=0, name='Major subsystem Version',
                  value=self.major_subsystem_version),
            Field(size=2, ph_address=0, name='Minor subsystem Version'
                  , value=self.minor_subsystem_version),
            Field(size=4, ph_address=20, name='ImageSize',
                  value=self.image_size),
            Field(size=4, ph_address=24, name='HeaderSize',
                  value=self.header_size),
            Field(size=4, ph_address=28, name='CheckSum',
                  value=self.check_sum),
            Field(size=2, ph_address=32, name='SubSystem',
                  value=self.subsystem),
            Field(size=2, ph_address=34, name='DllFlags',
                  value=self.dll_flags),
            Field(size=4, ph_address=36, name='StackReserveSize',
                  value=self.stack_reserve_size),
            Field(size=4, ph_address=40, name='StackCommitSize',
                  value=self.stack_commit_size),
            Field(size=4, ph_address=44, name='HeapReserveSize',
                  value=self.heap_reserve_size),
            Field(size=4, ph_address=48, name='HeapComitSize',
                  value=self.heap_comitSize),
            Field(size=4, ph_address=52, name='LoaderFlags',
                  value=self.loader_flags),
            Field(size=4, ph_address=56, name='DataDirSize',
                  value=self.data_dir_size),
        ]
        return fields
