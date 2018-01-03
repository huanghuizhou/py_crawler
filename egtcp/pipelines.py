# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

from egtcp.utils import to_dict


class GlobalSourcePipeline(object):
    def __init__(self):
        self.client = MongoClient(host='192.168.2.203', port=27017, username="gt_rw", password="greattao5877",
                                  authSource="dadaoDb",
                                  authMechanism="SCRAM-SHA-1")
        self.collection = self.client['dadaoDb']['test1']

    def process_item(self, item, spider):
        supplier_id = item['id']

        supplier = self.collection.find_one({'_id': supplier_id})
        if not supplier:
            data = dict(item)
            data['_id'] = data.pop('id')
            self.collection.insert_one(to_dict(data))
            return item

        return item
