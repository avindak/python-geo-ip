try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='geoip2nation',
    version='0.1.2',
    author='Avi Asher',
    author_email='aviasher@outlook.com',
    packages=['geoip'],
    package_data={'geoip': ['*.zip']},
    scripts=['geoip/geoip.py'],
    url='http://pypi.python.org/pypi/geoip2nation/',
    license='MIT',
    description='Convert ip addresses to a country using ip2nation db in memory.',
    long_description=open('README.md').read(),
)