#!usr/bin/env python
# coding:utf8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib
import json

headers = {}
headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400"

fr = open('../csv/films.txt', 'r')
films = []
for line in fr:
    line = json.loads(line.strip('\n'))
    films.append(line)
fr.close()

# 获取 characters,planets,starships,vehicles,species
targets = ['characters', 'planets', 'starships', 'vehicles', 'species']
for target in targets:
    fw = open('../csv/' + target + '.txt', 'w')
    data = []
    for item in films:
        tmp = item[target]
        for t in tmp:
            if t in data:
                continue
            else:
                data.append(t)
            while 1:
                print t
                try:
                    request = urllib2.Request(url=t, headers=headers)
                    response = urllib2.urlopen(request, timeout=20)
                    result = response.read()
                except Exception, e:
                    continue
                else:
                    fw.write(result + '\n')
                    break
                finally:
                    pass

    print str(len(data)), target
    fw.close()
