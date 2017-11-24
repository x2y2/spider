# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-
import MySQLdb
from pachong.jdconfig import JdConfig
 
class JdPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user = JdConfig['user'], 
                                    passwd = JdConfig['passwd'], 
                                    db = JdConfig['db'], 
                                    host = JdConfig['host'], 
                                    charset = 'utf8', 
                                    use_unicode = True)
        self.cursor = self.conn.cursor()
        # 清空表
        # self.cursor.execute('truncate table weather;')
        # self.conn.commit()
 
    def process_item(self, item, spider):
        for n,p,c,s in zip(item['name'],item['price'],item['commit'],item['shop']):
          try:
            self.cursor.execute(
                """INSERT IGNORE INTO phone (name,price,commit,shop)
                VALUES (%s, %s, %s, %s)""",(n,p,c,s))
            self.conn.commit()
          except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])
 
        return item
