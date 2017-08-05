# -*- coding: utf-8 -*-

# abuyun
proxyHost = "proxy.abuyun.com"
proxyPort = "9020"

proxyUser = "H3R3D6W03U3O049D"
proxyPass = "A34BB50E33A3EEFD"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = None

proxies_1 = {
    "http": proxyMeta,
    "https": proxyMeta,
}

proxies_3 = {
    # 'http': 'http://%s' % '219.234.81.111:9999',
    'http': 'http://%s' % '192.168.100.111:9999',
}

"""
___SEEKS_PROXY_USERID


___SEEKS_PROXY_ALLOW_CHANGE_IP

10.20.20.92:9999
"""