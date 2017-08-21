#!usr/bin/env python
# coding:utf8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import json

data = {}

fr = open('../csv/films.txt', 'r')

for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['title']] = tmp
fr.close()

fr = open('../csv/characters.txt', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()
fr = open('../csv/planets.txt', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()
fr = open('../csv/starships.txt', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()
fr = open('../csv/vehicles.txt', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()
fr = open('../csv/species.txt', 'r')
for line in fr:
    tmp = json.loads(line.strip('\n'))
    data[tmp['name']] = tmp
fr.close()

fw = open('../html/all.json', 'w')
fw.write(json.dumps(data))
fw.close()
