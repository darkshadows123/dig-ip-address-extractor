import unittest

# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from digExtractor.extractor_processor import ExtractorProcessor
from digIpAddressExtractor.ipaddress_extractor import IpAddressExtractor

class TestIpAddressExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ipaddress_extractor(self):
        doc = {'text' : 'my ip address is 192.168.0.1 and 193.14.1.1'}

        extractor = IpAddressExtractor().set_metadata({'extractor': 'ipaddress'})
        ep = ExtractorProcessor().set_input_fields(['text'])\
                                 .set_output_field('extracted')\
                                 .set_extractor(extractor)
        updated_doc = ep.extract(doc)
        result = updated_doc['extracted'][0]['result']
        self.assertEqual(result[0]['value'],
                         '192.168.0.1')
        self.assertEqual(result[1]['value'],
                         '193.14.1.1')

if __name__ == '__main__':
    unittest.main()
