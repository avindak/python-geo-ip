===========
Geo IP
===========

Note: This is a friendly Python 3 port of [python-geo-ip](https://github.com/avindak/python-geo-ip) by Avi Asher. We look forward to the original package supporting Python 3.

Provides a fast, seamless in memory ip to country functionality based on the ip2nation db.

- No dependencies
- Completely free
- Country resolution only
- Queries / sec > 13.5k per core
- Data file can be refreshed without a restart
- Memory footprint < 40 MB
- Command line
- Stream / pipe ips and get comma delimited [ip,2 letter country code] e.g. 12.12.12.12,US

```python
from geoip import geoip
r = geoip.GeoIp()
r.load_memory()
r.resolve("12.12.12.12").country_code
#This prints : 'US'

print r.resolve("123.44.57.4")
#This prints : {'country': 'Korea (South)', 'host_name': '', 'country_code': 'KR'}

r.resolve2("133.12.12.12")
#This prints : 'JP'
```

# Command line

usage: geoip.py [-h][-v] {download,resolve} ...

positional arguments:
{download,resolve}

optional arguments:
-h, --help show this help message and exit
-v, --verbose increase output verbosity

usage: geoip.py resolve [-h][-ho] [-s][--stream] ip

positional arguments:
ip The ip address to get the country for

optional arguments:
-h, --help show this help message and exit
-ho, --host When set to true the code will try to get the host name
-s, --short When set to true the code will return a 2 letter country code
only
--stream When set to true the code expect a stream of ips

usage: geoip.py download [-h]

optional arguments:
-h, --help show this help message and exit

# Installation

pip install geoip2nation

PyPI: https://pypi.python.org/pypi/geoip2nation/

Github: https://github.com/avindak/python-geo-ip

# ip2nation

- Data can be downloaded using the download method

- The load_memory method loads the ip2nation sql data file from disk into an in memory sqlite3 db

# license

MIT

# Links

- ip2nation home: http://ip2nation.com/
- ip2nation data file: http://www.ip2nation.com/ip2nation.zip
