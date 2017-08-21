#!usr/bin/env python
# coding:utf8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib
import json

films = []
for x in xrange(1,8):
    films.append('httP://swapi.co/api/films/' + str(x) + '/')

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400"

fw = open('../csv/films.txt', 'w')
for item in films:
    print item
    request = urllib2.Request(url=item, headers=headers)
    response = urllib2.urlopen(request, timeout=20)
    result = response.read()
    print result
    fw.write(result + '\n')

fw.close()