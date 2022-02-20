# meteomoris

get info about the weather in mauritius!

```
pip install meteomoris
```

# examples

```python
>>> from meteomoris import *

>>> get_weekforecast()
[{'condition': 'Few showers highgrounds',
     'date': 'Apr 22',
     'day': 'Mon',
     'max': '32�',
     'min': '21�',
     'probability': 'High',
     'sea condition': 'rough',
     'wind': 'E25G50'},
 {
...
 }
]

>>> get_weekforecast(day=3)
{'condition': 'Few passing showers',
 'date': 'Apr 25',
 'day': 'Thu',
 'max': '31�',
 'min': '20�',
 'probability': 'Medium',
 'sea condition': 'moderate',
 'wind': 'SE20'}

>>> get_weekforecast(day=3)['condition']
'Few passing showers'

>>> get_cityforecast()
{0: {'condition': 'Partly cloudy',
     'date': 'Apr 22',
     'day': 'Mon',
     'max': '31�',
     'min': '26�',
     'wind': 'E25G50'},
 1: {'condition': ...
}

>>> get_moonphase()
{'April 2019': {'first quarter': {'date': '12', 'hour': '23', 'minute': '06'},
                'full moon': {'date': '19', 'hour': '15', 'minute': '12'},
                'last quarter': {'date': '27', 'hour': '02', 'minute': '18'},
                'new moon': {'date': '05', 'hour': '12', 'minute': '50'}},
 'May 2019': {'first quarter': {'date': '12', 'hour': '05', 'minute': '12'},
...

>>> may = get_moonphase(month='May 2019')
>>> may['new moon']['date']
'05'
>>> get_sunrisemu()
{'february': {1: {'rise': '05:53', 'set': '18:53'},
              ...
              28: {'rise': '06:07', 'set': '18:37'}},
 'march': {1: {'rise': '06:07', 'set': '18:36'},
           2: {'rise': '06:07', 'set': '18:36'},
           ...
           31: {'rise': '06:16', 'set': '18:11'}
           }
}
>>> get_sunriserodr()
>>> get_sunrisemu().keys()
dict_keys(['february', 'march'])
```

# Local dev

In env

```
pip install -e . 
```

# Local test

In env

Install pytest `pip install pytest`

Run

`python -m pytest tests/`

# Changelog


### 2.0

- Added Meteo with classmethod workings
- Internet check
- Global settings
- Headers
- Sunrise and sunset for Mauritius and Rodrigues
- Basic tests