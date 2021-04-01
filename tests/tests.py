from __future__ import print_function
import unittest
import sys
sys.path.append('../code')
sys.path.append('../code/')
from geoip import GeoIp

class TestGeoIpMethods(unittest.TestCase):

    def test_resolve(self):
        ipr = GeoIp()
        ipr.load_memory()
        res = ipr.resolve("123.44.57.4")
        self.assertEqual(res.country_code, 'KR')

        res = ipr.resolve("34.73.223.65")
        self.assertEqual(res.country_code, 'US')

        res = ipr.resolve("109.64.149.83")
        self.assertEqual(res.country_code, 'IL')

    def test_resolve2(self):
        ipr = GeoIp()
        ipr.load_memory()
        res = ipr.resolve2("123.44.57.4")
        self.assertEqual(res, 'KR')

        res = ipr.resolve2("34.73.223.65")
        self.assertEqual(res, 'US')

        res = ipr.resolve2("109.64.149.83")
        self.assertEqual(res, 'IL')

    def test_download(self):
        ipr = GeoIp()
        downloaded = ipr.download()
        self.assertEqual(downloaded, True)

    def test_load_memory(self):
        ipr = GeoIp()
        self.assertEqual(ipr.loaded, False)
        ipr.load_memory()
        self.assertEqual(ipr.loaded, True)

    def test_dev(self):
        ipr = GeoIp(verbose=True)
        ipr.verbose = True
        print( ipr.resolve("109.64.149.83", True))
        ipr.download()
        ipr.load_memory()
        print(ipr.resolve("109.64.149.83", True))
        print( ipr.resolve("72.229.28.185", True))
        print( ipr.resolve("88.43.28.185", True))
        print( ipr.resolve("34.73.223.65", True))
        print( ipr.resolve("10.0.0.1", True))
        print( ipr.resolve("163.123.57.4"))
        print( ipr.resolve("123.44.57.4", True))
        print( ipr.resolve("0.0.0.0", True))




if __name__ == '__main__':
    unittest.main()