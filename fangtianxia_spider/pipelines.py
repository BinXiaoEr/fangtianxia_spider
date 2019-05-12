# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from .items import ESFItem,FangtianxiaItem
class FangtianxiaPipeline(object):
    def __init__(self):
        self.newhous=open('newhouse.json','wb')
        self.esfhousw=open('erfhous.json','wb')

    def process_item(self, item, spider):
        if isinstance(item,ESFItem):
            content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            self.esfhousw.write(content.encode('utf-8'))
            return item
        if isinstance(item,FangtianxiaItem):
            content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            self.newhous.write(content.encode('utf-8'))
            return item


