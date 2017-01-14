import json
import requests

VOTING_RESULTS_URL = 'http://api.scb.se/OV0104/v1/doris/sv/ssd/START/ME/ME0104/ME0104D/ME0104T4'


def get_region_highscores():
    voting_result_variables = retrieve_scb_voting_result_variables()
    region_code_map = create_region_code_map(voting_result_variables)
    riksdag_code = extract_riksdag_code(voting_result_variables)
    scb_region_data = retrieve_scb_region_voting_data_by_type(riksdag_code)
    return region_code_map


def create_region_code_map(voting_result_variables):
    value_texts = extract_value_texts(voting_result_variables)
    values = extract_values(voting_result_variables)
    return dict(zip(values, value_texts))


def extract_riksdag_code(scb_response):
    codes = extract_variable_data(scb_response, 'ContentsCode', 'values')
    value_texts = extract_variable_data(scb_response, 'ContentsCode', 'valueTexts')
    for item in zip(value_texts, codes):
        if 'riksdagsval' in item[0]:
            return item[1]


def extract_value_texts(scb_response):
    return extract_variable_data(scb_response, 'Region', 'valueTexts')


def extract_values(scb_response):
    return extract_variable_data(scb_response, 'Region', 'values')


def extract_variable_data(scb_response, variable_name, data_name):
    for x in scb_response['variables']:
        if x['code'] == variable_name:
            return x[data_name]


def retrieve_scb_voting_result_variables():
    response = requests.get(VOTING_RESULTS_URL)
    return json.loads(response.text)


def retrieve_scb_region_voting_data_by_type(riksdag_code):
    scb_region_data_request = create_region_data_request(riksdag_code)
    response = requests.post(VOTING_RESULTS_URL, scb_region_data_request)
    return json.loads(response.text)


def create_region_data_request(contents_code):
    return json.dumps({
        "query": [
            {
                "code": "Region",
                "selection": {
                    "filter": "all",
                    "values": ["*"]
                }
            },
            {
                "code": "ContentsCode",
                "selection": {
                    "filter": "item",
                    "values": [contents_code]
                }
            },
            {
                "code": "Tid",
                "selection": {
                    "filter": "item",
                    "values": ["*"]
                }
            }
        ],
        "response": {
            "format": "json"
        }
    })


if __name__ == '__main__':
    for item in get_region_highscores():
        print(item)
