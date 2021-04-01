try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='geoip2nation',
    version='0.2.6',
    author='Avi Asher',
    author_email='aviasher@outlook.com',
    packages=['geoip'],
    package_data={'geoip': ['*.zip']},
    scripts=['geoip/xgeoip.py'],
    url='http://pypi.python.org/pypi/geoip2nation/',
    license='MIT',
    description='Convert ip addresses to a country using ip2nation db in memory.',
    long_description=open('README.md').read(),
    long_description_content_type = 'text/markdown'
)