#!usr/bin/env python
# coding:utf8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import json

fr = open('../csv/films.txt','r')
fw = open('../csv/stat_basic.csv','w')

fw.write('title,key,value \n')

for line in fr:
    tmp = json.loads(line.strip('\n'))
    fw.write(tmp['title'] + ',' + 'characters,' + str(len(tmp['characters'])) + '\n')
    fw.write(tmp['title'] + ',' + 'planets,' + str(len(tmp['planets'])) + '\n')
    fw.write(tmp['title'] + ',' + 'starships,' + str(len(tmp['starships'])) + '\n')
    fw.write(tmp['title'] + ',' + 'vehicles,' + str(len(tmp['vehicles'])) + '\n')
    fw.write(tmp['title'] + ',' + 'species,' + str(len(tmp['species'])) + '\n')

fr.close()
fw.close()

