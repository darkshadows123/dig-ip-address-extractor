# -*- coding: utf-8 -*-
# @Author: darkshadows123

import copy
from digExtractor.extractor import Extractor
from dig_ipaddress_extractor import DIGIpAddressExtractor


class IpAddressExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']
        self.diae = DIGIpAddressExtractor()

    def extract(self, doc):
        if 'text' in doc:
            return self.diae.extract_ipaddress(doc['text'])
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields
