import struct
from tabulate import tabulate
from coff_header import COFFHeader
from dos_header import DOSHeader
from data_dir import DataDir
from export_table import ExportTable
from import_table import ImportTable
from optional_header import OptionalHeader
from section_header import SectionHeader


class HeaderInfo:
    def __init__(self):
        # О дос:
        self.dos_header_fmt = '<13HQHHQQIHI'
        dos_data = self.get_part_of_data(self.dos_header_fmt, 0)
        self.dos = DOSHeader(self.dos_header_fmt, dos_data)

        # О кофф:
        self.coff_header_fmt = '<IHHIIIH16B'  # H-2,I-4
        self.coff_start = self.dos.PE_header_address
        coff_data = self.get_part_of_data(self.coff_header_fmt, self.coff_start)
        self.coff = COFFHeader(self.coff_header_fmt, coff_data)

        # О пе:
        self.optional_header_fmt = '<HBB9I6H4IHH6I'
        self.coff_header_size = 24
        self.optional_header_start = self.coff_start + self.coff_header_size
        pe_data = self.get_part_of_data(self.optional_header_fmt,
                                        self.optional_header_start)
        self.pe = OptionalHeader(self.optional_header_fmt, pe_data)

        # о директориях:
        self.data_dir_fmt = '<22I'
        pe_size = 96
        self.data_dir_start = self.optional_header_start + pe_size
        data_dir_data = self.get_part_of_data(self.data_dir_fmt,
                                              self.data_dir_start)
        self.data_dir = DataDir(self.data_dir_fmt, data_dir_data)

        # О секциях:
        self.section_header_fmt = '<Q6I2H32B'
        self.number_of_section = self.coff.number_of_sections

    def get_part_of_data(self, fmt, offset):
        with open("resources/uninstall.exe", 'rb') as f:
            f.seek(offset)
            size = struct.calcsize(fmt)
            data = f.read(size)
        return data

    def format_fields(self, fields):
        table = tabulate([(field.size, field.ph_address,
                           field.name, field.value) for field in fields],
                         headers=["SIZE", "PH_ADDRESS",
                                  'NAME', "VALUE"], tablefmt='plain')
        return table

    def get_dos_header(self):
        fields = self.dos.get_dos_header_info()
        return self.format_fields(fields)

    def get_coff_header(self):
        fields = self.coff.get_coff_header_info()
        return self.format_fields(fields)

    def get_optional_header(self):
        fields = self.pe.get_optional_header_info()
        return self.format_fields(fields)

    def get_data_dir(self):
        fields = self.data_dir.get_data_dir_info()
        return self.format_fields(fields)

    def get_section_header(self, num_section):
        self.sections_start = (self.coff_start + self.coff_header_size
                               + self.coff.size_of_optional_header
                               + num_section * 40)
        self.section_data = self.get_part_of_data(self.section_header_fmt,
                                                  self.sections_start)
        self.section = SectionHeader(self.section_header_fmt,
                                     self.section_data)
        fields = self.section.get_section_header_info()
        return self.format_fields(fields)

    def find_import_offset(self, num_section):
        for i in range(1, num_section):
            self.sections_start = (self.coff_start + self.coff_header_size
                                   + self.coff.size_of_optional_header
                                   + i * 40)
            self.section_data = self.get_part_of_data(self.section_header_fmt,
                                                      self.sections_start)
            self.section = SectionHeader(self.section_header_fmt,
                                         self.section_data)
            fields = self.section.get_section_header_info()

            virtual_address = 0
            found_idata = False
            for field in fields:
                if field.name == "Name" and field.value == ".idata":
                    found_idata = True
                elif found_idata and field.name == "Virtual Address":
                    virtual_address = field.value
                elif found_idata and field.name == "Physical Address":
                    physical_address = field.value
                    return virtual_address, physical_address

        return None, None

    def process_import_table(self, virtual_address, physical_address):
        if virtual_address is None or physical_address is None:
            print("Import section not found")
            return

        import_table_rva = physical_address

        for _ in range(65535):
            data = self.get_part_of_data('<5I', import_table_rva)
            im = ImportTable('<5I', data)
            im.unpack_data()

            if im.all_zero():
                break

            dll_name = b''
            name_rva = im.name_rva
            name_offset = physical_address + (name_rva - virtual_address)

            if name_offset < 0:
                break

            for _ in range(256):
                byte = self.get_part_of_data('<1B', name_offset)
                if byte == b'\x00':
                    break
                dll_name += byte
                name_offset += 1

            print("DLL Name: ", dll_name.decode())

            import_table_rva += 20

    def find_export_offset(self, num_section):
        for i in range(1, num_section):
            self.sections_start = (self.coff_start + self.coff_header_size
                                   + self.coff.size_of_optional_header
                                   + i * 40)
            self.section_data = self.get_part_of_data(self.section_header_fmt,
                                                      self.sections_start)
            self.section = SectionHeader(self.section_header_fmt,
                                         self.section_data)
            fields = self.section.get_section_header_info()

            virtual_address = 0
            found_edata = False
            for field in fields:
                if field.name == "Name" and field.value == ".edata":
                    found_edata = True
                elif found_edata and field.name == "Virtual Address":
                    virtual_address = field.value
                elif found_edata and field.name == "Physical Address":
                    physical_address = field.value
                    return virtual_address, physical_address

        return None, None

    def process_export_table(self, virtual_address, physical_address):
        if virtual_address is None or physical_address is None:
            print(f"Export section not found")
            return

        data = self.get_part_of_data('<2I2H7I', physical_address)
        et = ExportTable('<2I2H7I', data)
        number_of_names = et.number_of_name_pointers
        name_pointer_table_rva = (physical_address + (et.name_pointer_rva - virtual_address))

        for i in range(number_of_names):
            name_data = self.get_part_of_data('<I', name_pointer_table_rva + i * 4)
            name_rva = struct.unpack('<I', name_data)[0]
            address = physical_address + (name_rva - virtual_address)

            func_name = b''

            for _ in range(256):
                byte = self.get_part_of_data('<1B', address)
                if byte == b'\x00':
                    break
                func_name += byte
                address += 1

            print(f"Function Name: {func_name.decode()}")
