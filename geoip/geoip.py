import sys
import os.path
import sqlite3
import urllib
import zipfile
from utillx import Utilx
from ipinfo import IpInfo
import argparse

class GeoIp(object):

    def __init__(self, data_source='http://www.ip2nation.com/ip2nation.zip', data_file=None, verbose=False):
        self.verbose = verbose
        self.conn = sqlite3.connect(':memory:')
        self.conn.text_factory = str
        #self.data_file = data_file
        if data_file is None:
            self.data_file = os.path.join(os.path.dirname(__file__), 'ip2nation.zip')
        else:
            self.data_file = data_file
        self.printv("Data file : {0}".format(self.data_file))
        self.data_source = data_source
        self.loaded = False

    def printv(self,s):
        if self.verbose:
            print s

    def download(self):
        self.printv("Download started...")
        self.printv("Url: {0}".format(self.data_source))


        urllib.urlretrieve(self.data_source, self.data_file)

        self.printv("Download completed")
        self.printv("File write completed")
        return True

    def load_memory(self):
        self.loaded = False
        self.printv("Load memory started...")
        if not os.path.exists(self.data_file):
            print "WARNING: The data file does not exists. Call download() to Download it."
            return

        try:
            z = zipfile.ZipFile(self.data_file)
        except zipfile.error, e:
            print "Bad zipfile (from %r): %s" % (self.data_file, e)
            self.loaded = False
            return

        for n in z.namelist():
            self.printv("File found in Zip : {0}".format(n))
            data = z.read(n)
            data = data.replace("ip int(11) unsigned NOT NULL default '0',", "\"ip\" integer ,")
            c = self.conn.cursor()
            c.executescript("""
                        DROP TABLE IF EXISTS ip2nation;

                        CREATE TABLE ip2nation (
                          ip int(11),
                          country char(2) NOT NULL default ''
                        );

                        DROP INDEX IF EXISTS ip_indx;

                        CREATE INDEX ip_indx ON ip2nation(ip);

                        DROP TABLE IF EXISTS ip2nationCountries;

                        CREATE TABLE ip2nationCountries (
                          code varchar(4) PRIMARY KEY,
                          iso_code_2 varchar(2) NOT NULL default '',
                          iso_code_3 varchar(3) default '',
                          iso_country varchar(255) NOT NULL default '',
                          country varchar(255) NOT NULL default '',
                          lat float NOT NULL default '0',
                          lon float NOT NULL default '0'
                        );

                        """)

            counter = 0
            for raw_line in data.split("\n"):
                if raw_line.startswith("INSERT"):
                    line = raw_line.replace("\\'", "")
                    #print line
                    c.executescript(line)
                    counter += 1

            self.conn.commit()
            c.close()

        z.close()
        self.printv("Load memory completed with {0} rows".format(counter))
        self.loaded = True

    def resolve2(self, ip_str):
        ipinfo = self.resolve(ip_str)
        return None if ipinfo is None else ipinfo.country_code


    def resolve(self, ip_str, auto_load=True, resolve_host_name=False):
        if not self.loaded:
            if auto_load:
                self.load_memory()
            else:
                print "WARNING : Ip data should be loaded before calling resolve"
            if not self.loaded:
                return None
        ip = Utilx.ip2inet(ip_str)
        query = """
         SELECT c.iso_code_2, c.country FROM
         ip2nationCountries c,
         ip2nation i
	        WHERE
	            i.ip < {0}
	            AND
	            c.code = i.country
	        ORDER BY
	            i.ip DESC
	        LIMIT 0,1;""".format(ip)

        c = self.conn.cursor()
        c.execute(query);
        res = c.fetchone()

        country_code = "" if res is None or len(res) == 0 else res[0]
        country = "" if res is None or len(res) == 0 else res[1]
        host_name = ""

        if resolve_host_name:
            host_name = Utilx.get_host(ip_str)

        info = IpInfo(country_code, country, host_name)
        return info


def download(args):
    ipr = GeoIp()
    ipr.verbose = True
    ipr.download()

def resolve(args):
    ipr = GeoIp()
    ipr.verbose = args.verbose
    ipr.load_memory()
    if args.stream:
        for line in sys.stdin:
            ip = line.strip()
            res = ipr.resolve(ip)
            sys.stdout.writelines("{0},{1}\n".format(ip, res.country_code))

    else:
        res = ipr.resolve(args.ip)
        if args.short:
            sys.stdout.writelines(res.country_code)
        else:
            sys.stdout.writelines(res)



parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")

subparsers = parser.add_subparsers()

download_parser = subparsers.add_parser('download')

resolve_parser = subparsers.add_parser('resolve')
resolve_parser.add_argument('ip',  help="The ip address to get the country for")  # add the name argument
resolve_parser.add_argument('-ho','--host',  help="When set to true the code will try to get the host name", action="store_true")  # add the name argument
resolve_parser.add_argument('-s','--short',  help="When set to true the code will return a 2 letter country code only", action="store_true")  # add the name argument
resolve_parser.add_argument('--stream',  help="When set to true the code expect a stream of ips", action="store_true")  # add the name argument
resolve_parser.set_defaults(func=resolve)  # set the default function to resolve



def main():
    args = parser.parse_args()
    args.func(args)  # call the default function




if __name__ == "__main__":
    main()
    #test()
