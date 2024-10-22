import struct
from field import Field


class COFFHeader:
    def __init__(self, fmt, coff_header_data):
        coff_header_values = struct.unpack(fmt, coff_header_data)

        byte_str = coff_header_data[:4]
        while byte_str.endswith(b'\x00'):
            byte_str = byte_str[:-1]

        self.magic = byte_str.decode()
        self.cpu_type = coff_header_values[1]
        self.number_of_sections = coff_header_values[2]
        self.time_date_stamp = coff_header_values[3]
        self.pointer_to_symbol_table = coff_header_values[4]
        self.number_of_symbols = coff_header_values[5]
        self.size_of_optional_header = coff_header_values[6]

        self.image_file_relocs_stripped = coff_header_values[7]
        self.image_file_executable_image = coff_header_values[8]
        self.image_file_line_nums_stripped = coff_header_values[9]
        self.image_file_local_syms_stripped = coff_header_values[10]
        self.image_file_aggressive_ws_trim = coff_header_values[11]
        self.image_file_large_address_aware = coff_header_values[12]
        self.reserved = coff_header_values[13]
        self.image_file_bytes_reversed_lo = coff_header_values[14]
        self.image_file_32bit_machine = coff_header_values[15]
        self.image_file_debug_stripped = coff_header_values[16]
        self.image_file_removable_run_from_swap = coff_header_values[17]
        self.image_file_net_run_from_swap = coff_header_values[18]
        self.image_file_system = coff_header_values[19]
        self.image_file_dll = coff_header_values[20]
        self.image_file_up_system_only = coff_header_values[21]
        self.image_file_bytes_reversed_hi = coff_header_values[22]

    def get_coff_header_info(self):
        fields = [
            Field(size=2, ph_address=0, name='Magic',
                  value=self.magic),
            Field(size=2, ph_address=2, name='CPUType',
                  value=self.cpu_type),
            Field(size=2, ph_address=4, name='Number of Sections',
                  value=self.number_of_sections),
            Field(size=4, ph_address=8, name='Time Date Stamp',
                  value=self.time_date_stamp),
            Field(size=4, ph_address=12, name='Pointer to Symbol Table',
                  value=self.pointer_to_symbol_table),
            Field(size=4, ph_address=16, name='Number of Symbols',
                  value=self.number_of_symbols),
            Field(size=2, ph_address=20, name='Size of Optional Header',
                  value=self.size_of_optional_header),
            Field(size=2, ph_address=22, name='IMAGE_FILE_RELOCS_STRIPPED',
                  value=self.image_file_relocs_stripped),
            Field(size=2, ph_address=24, name='IMAGE_FILE_EXECUTABLE_IMAGE',
                  value=self.image_file_executable_image),
            Field(size=2, ph_address=26, name='IMAGE_FILE_LINE_NUMS_STRIPPED',
                  value=self.image_file_line_nums_stripped),
            Field(size=2, ph_address=28, name='IMAGE_FILE_LOCAL_SYMS_STRIPPED',
                  value=self.image_file_local_syms_stripped),
            Field(size=2, ph_address=30, name='IMAGE_FILE_AGGRESIVE_WS_TRIM',
                  value=self.image_file_aggressive_ws_trim),
            Field(size=2, ph_address=32, name='IMAGE_FILE_LARGE_ADDRESS_AWARE',
                  value=self.image_file_large_address_aware),
            Field(size=2, ph_address=34, name='Reserved',
                  value=self.reserved),
            Field(size=2, ph_address=36, name='IMAGE_FILE_BYTES_REVERSED_LO',
                  value=self.image_file_bytes_reversed_lo),
            Field(size=2, ph_address=38, name='IMAGE_FILE_32BIT_MACHINE',
                  value=self.image_file_32bit_machine),
            Field(size=2, ph_address=40, name='IMAGE_FILE_DEBUG_STRIPPED',
                  value=self.image_file_debug_stripped),
            Field(size=2, ph_address=42,
                  name='IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP',
                  value=self.image_file_removable_run_from_swap),
            Field(size=2, ph_address=44, name='IMAGE_FILE_NET_RUN_FROM_SWAP',
                  value=self.image_file_net_run_from_swap),
            Field(size=2, ph_address=46, name='IMAGE_FILE_SYSTEM',
                  value=self.image_file_system),
            Field(size=2, ph_address=48, name='IMAGE_FILE_DLL',
                  value=self.image_file_dll),
            Field(size=2, ph_address=50, name='IMAGE_FILE_UP_SYSTEM_ONLY',
                  value=self.image_file_up_system_only),
            Field(size=2, ph_address=52, name='IMAGE_FILE_BYTES_REVERSED_HI',
                  value=self.image_file_bytes_reversed_hi)
        ]
        return fields
