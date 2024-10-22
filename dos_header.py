import struct

from field import Field


class DOSHeader:

    def __init__(self, fmt, dos_header_data):
        dos_header_values = struct.unpack(fmt, dos_header_data)
        self.magic = dos_header_data[:2].decode()
        self.bytes_on_last_page = dos_header_values[1]
        self.pages_in_file = dos_header_values[2]
        self.relocations = dos_header_values[3]
        self.size_of_header_in_paragraphs = dos_header_values[4]
        self.min_extra_paragraphs_needed = dos_header_values[5]
        self.max_extra_paragraphs_needed = dos_header_values[6]
        self.initial_relative_ss = dos_header_values[7]
        self.initial_sp = dos_header_values[8]
        self.checksum = dos_header_values[9]
        self.initial_ip = dos_header_values[10]
        self.initial_relative_cs = dos_header_values[11]
        self.file_address_of_relocation_table = dos_header_values[12]
        self.overlay_number = dos_header_values[13]
        self.oem_identifier = dos_header_values[14]
        self.oem_information = dos_header_values[15]
        self.PE_header_address = dos_header_values[20]

    def get_dos_header_info(self):
        fields = [
            Field(size=2, ph_address=0, name="Magic",
                  value=self.magic),
            Field(size=2, ph_address=2, name="Bytes on Last Page of File",
                  value=self.bytes_on_last_page),
            Field(size=2, ph_address=4, name="Pages in File",
                  value=self.pages_in_file),
            Field(size=2, ph_address=6, name="Relocations",
                  value=self.relocations),
            Field(size=2, ph_address=8, name="Size of Header in Paragraphs",
                  value=self.size_of_header_in_paragraphs),
            Field(size=2, ph_address=10,
                  name="Minimum Extra Paragraphs Needed",
                  value=self.min_extra_paragraphs_needed),
            Field(size=2, ph_address=12,
                  name="Maximum Extra Paragraphs Needed",
                  value=self.max_extra_paragraphs_needed),
            Field(size=2, ph_address=14, name="Initial Relative SS Value",
                  value=self.initial_relative_ss),
            Field(size=2, ph_address=16, name="Initial SP Value",
                  value=self.initial_sp),
            Field(size=2, ph_address=18, name="Checksum",
                  value=self.checksum),
            Field(size=2, ph_address=20, name="Initial IP Value",
                  value=self.initial_ip),
            Field(size=2, ph_address=22, name="Initial Relative CS Value",
                  value=self.initial_relative_cs),
            Field(size=2, ph_address=24,
                  name="File Address of Relocation Table",
                  value=self.file_address_of_relocation_table),
            Field(size=8, ph_address=26, name="Overlay Number",
                  value=self.overlay_number),
            Field(size=2, ph_address=34, name="OEM Identifier",
                  value=self.oem_identifier),
            Field(size=2, ph_address=36, name="OEM Information",
                  value=self.oem_information),
            Field(size=4, ph_address=60, name="PE Header Address",
                  value=self.PE_header_address)
        ]
        return fields
