# pyStatsNZ
Python wrapper for prototype [StatisticsNZ API](https://statisticsnz.portal.azure-api.net/). Thanks to Jonathon Marshall for his [R wrapper package](https://github.com/jmarshallnz/statsNZ), which provided guidance and inspiration.


## Installation

PyStatsNZ uses the popular [requests](http://docs.python-requests.org/en/master/) module. Recommended installation is using a [virtualenv via pip](http://docs.python-guide.org/en/latest/dev/virtualenvs/):

1. Create and activate your virtual environment (e.g. `virtualenv venv` then `source venv/bin/activate`)
2. Install requests with the requirements file: `pip install -r requirements.txt`

## Basic usage

`>>> import pystatsnz, credentials`

Set up an instance of the API with your primary StatsNZ key. For convenience, you can keep your StatsNZ API key in `credentials.py`.

`>>> api = pystatsnz.Api(credentials.statsnz_key)`

Get a list of the shortcodes used to signify each dataset:

```
>>> print(api.list_dataset_codes())

['ALC', 'BOP', 'BPI', 'CRT', 'ESM', 'GDP', 'GDPRgional', 'GST', 'LMS', 'NACFCentralGovernment', 'NACFLocalGovernment', 'OTI', 'ProductivityStatistics', 'RTS', 'VBW', 'WTS']
```

Get a dataset's descriptive name:

```
>>> print(api.get_dataset_name('ALC'))

Alcohol available for Consumption
```

Get all data relating to a specific dataset and print the first few results to the console:

```
>>> from pprint import pprint as pp
>>> alc = api.get_group_data('ALC')
>>> pp(alc[:5])

[{u'DataValues': u'6.389809',
  u'Group': u'Litres of Alcohol',
  u'Id': 7900,
  u'Magnitude': u'6',
  u'Period': u'1998.09',
  u'SeriesReference': u'ALCA.SALFAS',
  u'SeriesTitle1': u'Grape wine containing not more than 14% alc.',
  u'Suppressed': None,
  u'Unit': u'Litres',
  u'status': u'FINAL'},
 {u'DataValues': u'6.794944',
  u'Group': u'Litres of Alcohol',
  ...
]
```

Get a list of the unique groups for a specific dataset and print the first few results to the console:

```
>>> fields = api.get_dataset_groups('ALC')
>>> pp(fields)

[u'Litres of Beverage',
 u'Litres of Alcohol',
 u'Litres of Alcohol Per Head of Population - by alcohol type']
```

Scope a data request to a specific group and print first few results to the console:

```
>>> alc_subset = api.get_group_data('ALC', 'Litres of Alcohol Per Head of Population - by alcohol type')
>>> pp(alc_subset[:5])

[{u'DataValues': u'0.317962792',
  u'Group': u'Litres of Alcohol Per Head of Population - by alcohol type',
  u'Id': 5072,
  u'Magnitude': u'0',
  u'Period': u'2014.12',
  u'SeriesReference': u'ALCQ.SALV',
  u'SeriesTitle1': u'Total N.Z. Population for Spirits containing more than 23% alcohol',
  u'Suppressed': None,
  u'Unit': u'Litres',
  u'status': u'FINAL'},
 {u'DataValues': u'0.241498648',
  u'Group': u'Litres of Alcohol Per Head of Population - by alcohol type',
  ...
]
```
