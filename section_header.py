import struct
from field import Field


class SectionHeader:
    def __init__(self, fmt, section_header_data):
        section_header_values = struct.unpack(fmt, section_header_data)

        byte_str = section_header_data[:8]
        while byte_str.endswith(b'\x00'):
            byte_str = byte_str[:-1]
        self.name = byte_str.decode()
        self.virtual_size = section_header_values[1]
        self.virtual_address = section_header_values[2]
        self.physical_size = section_header_values[3]
        self.physical_address = section_header_values[4]
        self.physical_address = section_header_values[4]
        self.physical_address = section_header_values[4]
        self.physical_address = section_header_values[4]
        self.physical_address = section_header_values[4]

        self.image_scn_type_no_pad = section_header_values[5]
        self.image_scn_cnt_code = section_header_values[6]
        self.image_scn_cnt_initialized_data = section_header_values[7]
        self.image_scn_cnt_uninitialized_data = section_header_values[8]
        self.image_scn_lnk_other = section_header_values[9]
        self.image_scn_lnk_info = section_header_values[10]
        self.image_scn_lnk_remove = section_header_values[11]
        self.image_scn_lnk_comdat = section_header_values[12]
        self.image_scn_gprel = section_header_values[13]
        self.image_scn_mem_purgeable = section_header_values[14]
        self.image_scn_mem_16bit = section_header_values[15]
        self.image_scn_mem_locked = section_header_values[16]
        self.image_scn_mem_preload = section_header_values[17]
        self.image_scn_align_1bytes = section_header_values[18]
        self.image_scn_align_2bytes = section_header_values[19]
        self.image_scn_align_4bytes = section_header_values[20]
        self.image_scn_align_8bytes = section_header_values[21]
        self.image_scn_align_16bytes = section_header_values[22]
        self.image_scn_align_32bytes = section_header_values[23]
        self.image_scn_align_64bytes = section_header_values[24]
        self.image_scn_align_128bytes = section_header_values[25]
        self.image_scn_align_256bytes = section_header_values[26]
        self.image_scn_align_512bytes = section_header_values[27]
        self.image_scn_align_1024bytes = section_header_values[28]
        self.image_scn_align_2048bytes = section_header_values[29]
        self.image_scn_align_4096bytes = section_header_values[30]
        self.image_scn_align_8192bytes = section_header_values[31]
        self.image_scn_lnk_nreloc_ovfl = section_header_values[32]
        self.image_scn_mem_discardable = section_header_values[33]
        self.image_scn_mem_not_cached = section_header_values[34]
        self.image_scn_mem_not_paged = section_header_values[35]
        self.image_scn_mem_shared = section_header_values[36]

    def get_section_header_info(self):
        fields = [
            Field(size=8, ph_address=0, name='Name',
                  value=self.name),
            Field(size=4, ph_address=2, name='Virtual Size',
                  value=self.virtual_size),
            Field(size=4, ph_address=2, name='Virtual Address',
                  value=self.virtual_address),
            Field(size=4, ph_address=2, name='Physical Size',
                  value=self.physical_size),
            Field(size=4, ph_address=2, name='Physical Address',
                  value=self.physical_address),
            Field(size=4, ph_address=0, name='IMAGE_SCN_TYPE_NO_PAD',
                  value=self.image_scn_type_no_pad),
            Field(size=4, ph_address=0, name='IMAGE_SCN_CNT_CODE',
                  value=self.image_scn_cnt_code),
            Field(size=1, ph_address=0, name='IMAGE_SCN_CNT_INITIALIZED_DATA',
                  value=self.image_scn_cnt_initialized_data),
            Field(size=1, ph_address=0,
                  name='IMAGE_SCN_CNT_UNINITIALIZED_DATA',
                  value=self.image_scn_cnt_uninitialized_data),
            Field(size=1, ph_address=0, name='IMAGE_SCN_LNK_OTHER',
                  value=self.image_scn_lnk_other),
            Field(size=1, ph_address=0, name='IMAGE_SCN_LNK_INFO',
                  value=self.image_scn_lnk_info),
            Field(size=1, ph_address=0, name='IMAGE_SCN_LNK_REMOVE',
                  value=self.image_scn_lnk_remove),
            Field(size=1, ph_address=0, name='IMAGE_SCN_LNK_COMDAT',
                  value=self.image_scn_lnk_comdat),
            Field(size=1, ph_address=0, name='IMAGE_SCN_GPREL',
                  value=self.image_scn_gprel),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_PURGEABLE',
                  value=self.image_scn_mem_purgeable),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_16BIT',
                  value=self.image_scn_mem_16bit),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_LOCKED',
                  value=self.image_scn_mem_locked),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_PRELOAD',
                  value=self.image_scn_mem_preload),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_1BYTES',
                  value=self.image_scn_align_1bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_2BYTES',
                  value=self.image_scn_align_2bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_4BYTES',
                  value=self.image_scn_align_4bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_8BYTES',
                  value=self.image_scn_align_8bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_16BYTES',
                  value=self.image_scn_align_16bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_32BYTES',
                  value=self.image_scn_align_32bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_64BYTES',
                  value=self.image_scn_align_64bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_128BYTES',
                  value=self.image_scn_align_128bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_256BYTES',
                  value=self.image_scn_align_256bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_512BYTES',
                  value=self.image_scn_align_512bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_1024BYTES',
                  value=self.image_scn_align_1024bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_2048BYTES',
                  value=self.image_scn_align_2048bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_4096BYTES',
                  value=self.image_scn_align_4096bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_ALIGN_8192BYTES',
                  value=self.image_scn_align_8192bytes),
            Field(size=1, ph_address=0, name='IMAGE_SCN_LNK_NRELOC_OVFL',
                  value=self.image_scn_lnk_nreloc_ovfl),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_DISCARDABLE',
                  value=self.image_scn_mem_discardable),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_NOT_CACHED',
                  value=self.image_scn_mem_not_cached),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_NOT_PAGED',
                  value=self.image_scn_mem_not_paged),
            Field(size=1, ph_address=0, name='IMAGE_SCN_MEM_SHARED',
                  value=self.image_scn_mem_shared),
        ]
        return fields

    def find_idata_info(self):
        return self.physical_address