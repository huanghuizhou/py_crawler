#!/usr/bin/env python3
# coding=utf-8


from pymongo import MongoClient

DB_NAME = 'dadaoDb'
COLLECTION_NAME = 'GlobalSourceSuppliers'

MONGO_CLIENT = MongoClient(host='192.168.2.203', port=27017, username="gt_rw", password="greattao5877",
                           authSource=DB_NAME,
                           authMechanism="SCRAM-SHA-1")