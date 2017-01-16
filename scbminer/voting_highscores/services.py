import json
import requests

# URLs should be put in some configuration
VOTING_RESULTS_URL = 'http://api.scb.se/OV0104/v1/doris/sv/ssd/START/ME/ME0104/ME0104D/ME0104T4'
VALUE_COLUMN = 'c'


def get_region_highscores():
    voting_result_variables = retrieve_scb_voting_result_variables()
    region_code_map = create_region_code_map(voting_result_variables)
    riksdag_code = extract_riksdag_code(voting_result_variables)
    scb_region_data = retrieve_scb_voting_data_by_type(riksdag_code)
    voting_results = extract_voting_results_by_year(scb_region_data,
                                                    region_code_map)
    return voting_results


def extract_voting_results_by_year(scb_region_data, region_code_map):
    """ Extracts and returns a dictionary with year as key and
        the area with highest turnout rate as value """
    data_keys = extract_data_keys(scb_region_data)
    results = {}
    year_index = data_keys['Tid']
    region_index = data_keys['Region']

    for data in scb_region_data['data']:
        year = data['key'][year_index]
        region_name = region_code_map[data['key'][region_index]]
        value = data['values'][0]
        results.setdefault(year, []).append((region_name, value))

    for years in results.keys():
        results[years].sort(key=lambda result: result[1], reverse=True)
        results[years] = results[years][0]

    return results


def extract_data_keys(scb_region_data):
    """ This map is used to keep track of what index the data has """
    columns = list(enumerate(scb_region_data['columns']))
    data_keys = [(column['code'], i) for (i, column) in columns
                 if column['type'] != VALUE_COLUMN]
    return dict(data_keys)


def create_region_code_map(voting_result_variables):
    """ This map is used to identify what codes each region has """
    value_texts = extract_value_texts(voting_result_variables)
    values = extract_values(voting_result_variables)
    return dict(zip(values, value_texts))


def extract_riksdag_code(scb_response):
    codes = extract_variable_data(scb_response, 'ContentsCode', 'values')
    value_texts = extract_variable_data(scb_response,
            'ContentsCode', 'valueTexts')

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


def retrieve_scb_voting_data_by_type(riksdag_code):
    scb_region_data_request = create_region_data_request(riksdag_code)
    response = requests.post(VOTING_RESULTS_URL, scb_region_data_request,
                             stream=True)
    # Due to some bug, json cannot load this response due to a BOM header
    # without explicit decoding.
    return json.loads(response.raw.read().decode('utf-8-sig'))


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
                    "filter": "all",
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
