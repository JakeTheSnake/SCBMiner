import unittest
import services
import json


EXAMPLE_RESPONSE = json.loads("""{
  \"title\": \"Valdeltagande efter region, tabellinnehåll och valår\",
  \"variables\": [
    {
      \"code\": \"Region\",
      \"text\": \"region\",
      \"values\": [
        \"00\",
        \"0114\",
        \"0115\"
      ],
      \"valueTexts\": [
        \"Riket\",
        \"Upplands Väsby\",
        \"Vallentuna\"
      ]
    },
    {
      \"code\": \"ContentsCode\",
      \"text\": \"tabellinnehåll\",
      \"values\": [
        \"ME0104B8\",
        \"ME0104C5\",
        \"ME0104C6\"
      ],
      \"valueTexts\": [
        \"Valdeltagande i riksdagsval, procent\",
        \"Valdeltagande i landstingsfullmäktigval, procent\",
        \"Valdeltagande i kommunfullmäktigval, procent\"
      ]
    },
    {
      \"code\": \"Tid\",
      \"text\": \"valår\",
      \"values\": [
        \"1973\",
        \"1976\"
      ],
      \"valueTexts\": [
        \"1973\",
        \"1976\"
      ],
      \"time\": true
    }
  ]
}""")


class TestServices(unittest.TestCase):

    def test_that_region_value_texts_can_be_extracted(self):
        actual_value_texts = services.extract_value_texts(EXAMPLE_RESPONSE)
        self.assertEquals(len(actual_value_texts), 3)
        self.assertEquals(actual_value_texts[0], 'Riket')
        self.assertEquals(actual_value_texts[1], 'Upplands Väsby')
        self.assertEquals(actual_value_texts[2], 'Vallentuna')

    def test_that_region_values_can_be_extracted(self):
        actual_value_texts = services.extract_values(EXAMPLE_RESPONSE)
        self.assertEquals(len(actual_value_texts), 3)
        self.assertEquals(actual_value_texts[0], '00')
        self.assertEquals(actual_value_texts[1], '0114')
        self.assertEquals(actual_value_texts[2], '0115')

    def test_that_region_code_map_can_be_extracted(self):
        region_code_map = services.create_region_code_map(EXAMPLE_RESPONSE)
        self.assertEquals(region_code_map['00'], 'Riket')
        self.assertEquals(region_code_map['0114'], 'Upplands Väsby')
        self.assertEquals(region_code_map['0115'], 'Vallentuna')

    def test_that_riksdags_code_can_be_extracted_from_response(self):
        actual_riksdag_code = services.extract_riksdag_code(EXAMPLE_RESPONSE)
        self.assertEqual(actual_riksdag_code, 'ME0104B8')


if __name__ == '__main__':
    unittest.main()
