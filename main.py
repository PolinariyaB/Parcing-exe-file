from header_info import HeaderInfo
from import_table import ImportTable
from parser import Parser


def main():
    parser = Parser()

    header_info = HeaderInfo()
    (header_type, num) = parser.parse_arguments()

    if header_type == 'dos':
        print(header_info.get_dos_header())
    elif header_type == 'coff':
        print(header_info.get_coff_header())
    elif header_type == 'pe':
        print(header_info.get_optional_header())
    elif header_type == 'dir':
        print(header_info.get_data_dir())
    elif header_type == 'section':
        if (num > header_info.number_of_section - 1):
            print("неверное количество секций")
        else:
            print(header_info.get_section_header(num))
    elif header_type == 'im':
        virtual_address, physical_address = \
            header_info.find_import_offset(header_info.number_of_section)
        header_info.process_import_table(virtual_address, physical_address)
    elif header_type == 'ex':
        v_address, f_address = \
            header_info.find_export_offset(header_info.number_of_section)
        header_info.process_export_table(v_address, f_address)


main()
