# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Scrapyp1Pipeline(object):

    def __init__(self):
        self.file = open("E:/Users/zhaocc/PycharmProjects/scrapyP1/test.json", "w")

    def process_item(self, item, spider):
        line = "school: %s, name: %s, src:%s\n" % (item['school'][0], item['name'][0], item['src'][0])
        print("process_item line: %s" % line)
        self.file.write(line)
        return item
