
class IpInfo(object):

    def __init__(self, country_code, country, host_name):
        self.country_code = country_code
        self.country = country
        self.host_name = host_name

    def __str__(self):
        return "{0}".format(self.__dict__)
