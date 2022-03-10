# meteomoris

get info about the weather in mauritius!

```
pip install meteomoris
```

Venv explanations at footer.

# Examples

```python
>>> from meteomoris import *

>>> get_main_message()
"A Strong Wind Warning and High Wave Warning for Mauritius | Aucun avertissement de cyclone n'est en vigueur a Maurice | Avertissement de fortes houles pour Rodrigues"

>>> get_weekforecast()
[
 {'condition': 'Few showers highgrounds',
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
[
 {'condition': 'Partly cloudy',
     'date': 'Apr 22',
     'day': 'Mon',
     'max': '31�',
     'min': '26�',
     'wind': 'E25G50'},
 {'condition': ...}
]


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
{
 'february': {
                1: {'rise': '05:53', 'set': '18:53'},
                ...
                28: {'rise': '06:07', 'set': '18:37'}
            },
 'march': {
            1: {'rise': '06:07', 'set': '18:36'},
            2: {'rise': '06:07', 'set': '18:36'},
            ...
            31: {'rise': '06:16', 'set': '18:11'}
        }
}

>>> get_sunriserodr()

>>> get_sunrisemu().keys()
dict_keys(['february', 'march'])

>>> get_eclipses()
[
 {
    'end': {'date': 1, 'hour': 2, 'minute': 37, 'month': 'may'},
    'info': 'The eclipse will not be visible in Mauritius, Rodrigues, St. Brandon and Agalega.',
    'start': {'date': 30, 'hour': 22, 'minute': 45, 'month': 'april'},
    'status': 'partial',
    'type': 'sun'
 },
 ...
 {
    'end': {'date': 8, 'hour': 17, 'minute': 56, 'month': 'november'},
    'info': 'The eclipse will not be visible in Mauritius, Rodrigues, St. Brandon and Agalega.',
    'start': {'date': 8, 'hour': 12, 'minute': 2, 'month': 'november'},
    'status': 'total',
    'type': 'moon'
 }
]

>>> get_equinoxes()
[
 {
    'day': 20, 'hour': 19, 'minute': 33, 'month': 'march', 'year': 2022
 },
 {
  'day': 23, 'hour': 5, 'minute': 3, 'month': 'september', 'year': 2022
 }
]

>>> get_solstices()
[
 {
    'day': 21, 'hour': 13, 'minute': 13, 'month': 'june', 'year': 2022
 },
 {
    'day': 22, 'hour': 1, 'minute': 48, 'month': 'december', 'year': 2022
 }
]


```

# Global settings

```python
from meteomoris import Meteo
from meteomoris import get_main_message

Meteo.CHECK_INTERNET = True # Will check if there is internet
Meteo.EXIT_ON_NO_INTERNET = True # Will exit if no internet
Meteo.headers = {
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',
         'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
         'Accept-Language' : 'en-US,en;q=0.5', 
         'Accept-Encoding' : 'gzip', 
         'DNT' : '1', # Do Not Track Request Header 
         'Connection' : 'close',
         'Sec-GPC': '1',
         'Sec-Fetch-Site': 'none',
         'Sec-Fetch-Mode': 'navigate',
         'Sec-Fetch-User': '?1',
         'Connection': 'keep-alive',
         'Upgrade-Insecure-Requests': '1'
     } # Redefine default headers here

print(get_main_message())
```
# Installing

Create and activate env

Linux 

```
python3.9 -m venv venv
. venv/bin/activate
```

Windows

```
py -3.9 -m venv venv
venv\Scripts\activate.bat :: for command prompt
venv\Scripts\Activate.ps1 :: for powershell
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


## 2.1.0

- Fix get_moonphase
- Add get_equinoxes
- Add get_solstices
- Add get_equinoxes

## 2.0.2

- Fix broken install

### 2.0.1


- Add venv docs
- Add global settings docs

### 2.0.0

- Add Meteo with classmethod
- Add internet check
- Add global settings
- Add headers change option
- Add get_sunrisemu
- Add get_sunriserodr
- Tests basics