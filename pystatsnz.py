import csv, json
from requests import get

from pprint import pprint as pp

# TODO: fix this shortcut to suppress insecure platform errors
# see http://stackoverflow.com/questions/29099404/ssl-insecureplatform-error-when-using-requests-package
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

class Api():
    def __init__(self, api_key=None, verbose=True, version='v0.1'):
        """Create a new API object with API key, base_url & verbosity flag"""
        if api_key:
            self.api_key = api_key
        else:
            raise ValueError('StatisticsNZ API requires an api key.')
        self.base_url = 'https://statisticsnz.azure-api.net/data'
        self.version = version
        self.verbose = verbose

        # ideally groups data should be pulled from StatsNZ, not hardcoded here
        self.groups = {
            'ALC': 'Alcohol available for Consumption',
            'BOP': 'Balance of Payments and International Investment Position',
            'BPI': 'Business Price Indexes',
            'CRT': 'Christchurch Retail Trade Indicator',
            'ESM': 'Economic Survey of Manufacturing',
            'GDP': 'Gross Domestic Product',
            'GDPRgional': 'Regional Gross Domestic Product',
            'GST': 'Goods and Services Trade by Country',
            'LMS': 'Labour Market Statistics',
            'NACFCentralGovernment':'Government Finance Statistics (Central Government)',
            'NACFLocalGovernment':'Government Finance Statistics (Local Government)',
            'OTI': 'Overseas Trade Indexes (Prices and Volumes)',
            'ProductivityStatistics': 'Productivity Statistics',
            'RTS': 'Retail Trade Survey',
            'VBW': 'Value of Building Work Put in Place',
            'WTS': 'Wholesale Trade Survey',
        }

    def list_dataset_codes(self):
        """ Get a list of all dataset codes. """
        codes = self.groups.keys()
        codes.sort()
        return codes

    def get_dataset_name(self, code):
        """ Get the name of a dataset from it's group code. """
        return  self.groups.get(code)

    def get_dataset_groups(self, code):
        """ Get a list of all groups for a dataset. """
        url = '{}/{}/{}/groups'.format(self.base_url, code, self.version)
        return self.fetch_json(url)

    def get_group_data(self, code, group=None):
        """ Get statistical data for one or all groups in a dataset. """
        url = '{}/api/{}'.format(self.base_url, code)
        params = {'groupName':group}
        return self.fetch_json(url, params=params)


    def fetch_json(self, url, params={}):
        """ Construct HTTP request & fetch JSON from StatsNZ API """
        headers = {'Ocp-Apim-Subscription-Key': self.api_key}
        response = get(url, headers=headers, params=params)
        if self.verbose:
            print('Fetched: {}'.format(response.url))
        self.errors = None
        if response.status_code == 200:
            if self.verbose:
                print('Retrieved: {} rows'.format( len(response.json()) ))
            return response.json()
        else:
            print('ERROR: Status code {} while retrieving {}'.format(response.status_code, response.url))
            return None


def main():
    pass

if __name__ == '__main__':
    main()
