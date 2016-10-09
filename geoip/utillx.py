import socket


class Utilx(object):

    @staticmethod
    def ip2inet(ip):
        original_ip = ip
        try:
            # 42.60.159.15, 220.255.2.170
            if "," in ip:
                proxy_tokens = ip.split(',')
                if "." in proxy_tokens[len(proxy_tokens) - 1]:
                    ip = proxy_tokens[len(proxy_tokens) - 1]
                else:
                    ip = proxy_tokens[len(proxy_tokens) - 2]

            tokens = ip.split('.')
            inet = long(tokens[0]) * 16777216 + long(tokens[1]) * 65536 + long(tokens[2]) * 256 + long(tokens[3])
            return inet
        except:
            print "Error in ip2inet for ip: {0}".format(original_ip)
            return 0

    @staticmethod
    def get_host(ip):
        try:
            hn = socket.gethostbyaddr(ip)
        except socket.herror:
            hn = ()

        if len(hn) > 0:
            host_name = hn[0]
        else:
            host_name = ip

        return host_name
