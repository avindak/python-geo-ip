===========
Geo IP
===========

Provides a fast, seamless in memory ip to country functionality based on the ip2nation db.

```python
from geoip import geoip
r = geoip.GeoIp()
r.load_memory()
r.resolve("12.12.12.12").country_code
#This prints : 'US'

print r.resolve("123.44.57.4")
#This prints : {'country': 'Korea (South)', 'host_name': '', 'country_code': 'KR'}

r.resolve2("12.12.12.12").country_code
#This prints : 'US'
```


Installation
=========

pip install geoip2nation

https://pypi.python.org/pypi/geoip2nation/

ip2nation
=========

* Data can be downloaded using the download method

* The load_memory method loads the ip2nation sql data file from disk into an in memory sqlite3 db

license
========
MIT

Links
========

ip2nation home http://ip2nation.com/