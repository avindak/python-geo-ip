import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import twine
except ImportError:
    raise ImportError("Please run: pip install twine")

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    os.system("git tag -a %s -m 'version %s'" % (__version__, __version__))
    os.system("git push --tags")
    sys.exit()

setup(
    name="geoip2nation3",
    version="0.2.0",
    author="Daniel Roy Greenfeld",
    author_email="pydanny@gmail.com",
    packages=["geoip"],
    package_data={"geoip": ["*.zip"]},
    scripts=["geoip/geoip.py"],
    url="https://github.com/pydanny/geoip2nation",
    license="MIT",
    description="Convert ip addresses to a country using ip2nation db in memory.",
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
