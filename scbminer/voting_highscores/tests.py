import unittest
import services
from scb_test_data import *


class TestServices(unittest.TestCase):

    def test_that_region_value_texts_can_be_extracted(self):
        actual_value_texts = services.extract_value_texts(VARIABLES_RESPONSE)
        self.assertEqual(len(actual_value_texts), 3)
        self.assertEqual(actual_value_texts[0], 'Riket')
        self.assertEqual(actual_value_texts[1], 'Upplands Väsby')
        self.assertEqual(actual_value_texts[2], 'Vallentuna')

    def test_that_region_values_can_be_extracted(self):
        actual_value_texts = services.extract_values(VARIABLES_RESPONSE)
        self.assertEqual(len(actual_value_texts), 3)
        self.assertEqual(actual_value_texts[0], '00')
        self.assertEqual(actual_value_texts[1], '0114')
        self.assertEqual(actual_value_texts[2], '0115')

    def test_that_region_code_map_can_be_extracted(self):
        region_code_map = services.create_region_code_map(VARIABLES_RESPONSE)
        self.assertEqual(region_code_map['00'], 'Riket')
        self.assertEqual(region_code_map['0114'], 'Upplands Väsby')
        self.assertEqual(region_code_map['0115'], 'Vallentuna')

    def test_that_riksdags_code_can_be_extracted_from_response(self):
        actual_riksdag_code = services.extract_riksdag_code(VARIABLES_RESPONSE)
        self.assertEqual(actual_riksdag_code, 'ME0104B8')

    def test_that_data_keys_can_be_extracted_from_voting_results(self):
        actual_data_keys = services.extract_data_keys(DATA_RESPONSE);
        self.assertEqual(len(actual_data_keys), 2)
        self.assertEqual(actual_data_keys['Region'], 0)
        self.assertEqual(actual_data_keys['Tid'], 1)

    def test_that_voting_results_are_extracted_from_response(self):
        code_map = services.create_region_code_map(VARIABLES_RESPONSE)
        actual_results = services.extract_voting_results_by_year(DATA_RESPONSE,
                                                                 code_map)

        self.assertEqual(actual_results['1973'][0][0], 'Vallentuna')
        self.assertEqual(actual_results['1973'][0][1], '93.3')
        self.assertEqual(actual_results['1973'][1][0], 'Upplands Väsby')
        self.assertEqual(actual_results['1973'][1][1], '91.4')
        self.assertEqual(actual_results['2014'][0][0], 'Vallentuna')
        self.assertEqual(actual_results['2014'][0][1], '89.3')
        self.assertEqual(actual_results['2014'][1][0], 'Upplands Väsby')
        self.assertEqual(actual_results['2014'][1][1], '84.1')


if __name__ == '__main__':
    unittest.main()
