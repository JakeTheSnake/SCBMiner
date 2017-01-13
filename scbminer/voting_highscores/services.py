import json
import requests

VOTING_RESULTS_URL = 'http://api.scb.se/OV0104/v1/\
                      doris/sv/ssd/START/ME/ME0104/ME0104D/ME0104T4'


def get_region_highscores():
    data_definitions = get_stuff()
    region_code_map = zip(data_definitions.variables)


def get_stuff():
    response = requests.get(VOTING_RESULTS_URL)
    return json.loads(response.text)


if __name__ == '__main__':
    print(get_region_highscores())
