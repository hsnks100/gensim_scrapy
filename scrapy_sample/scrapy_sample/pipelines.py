# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from __future__ import unicode_literals
import json
import codecs

from konlpy.tag import Kkma
from konlpy.utils import pprint
import jpype 
from konlpy.tag import Twitter

class Apt2UPipeline(object):
    def __init__(self):
        self.file = codecs.open('corpus/cp.json', 'w', encoding='utf-8')
         
    def process_item(self, item, spider):
        twitter = Twitter()
        outputList = twitter.pos(item['pagetitle'].strip())
        line = ''

        for (a, b) in outputList:
            line += a + "/" + b + " "
		
        print line

        self.file.write(line) #파일에 기록
        print item['pagetitle']
        return item
         
    def spider_closed(self, spider):
        self.file.close()   #파일 CLOSE
