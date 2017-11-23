# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-
import MySQLdb
import datetime
from pachong.myconfig import DbConfig
 
class DBPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user = DbConfig['user'], 
                                    passwd = DbConfig['passwd'], 
                                    db = DbConfig['db'], 
                                    host = DbConfig['host'], 
                                    charset = 'utf8', 
                                    use_unicode = True)
        self.cursor = self.conn.cursor()
        # 清空表
        # self.cursor.execute('truncate table weather;')
        # self.conn.commit()
 
    def process_item(self, item, spider):
        curTime = datetime.datetime.now()
        try:
            self.cursor.execute(
                """INSERT IGNORE INTO movies (rank,title,link,pic,star,rate,quote)
                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (
                    item['rank'],
                    item['title'],
                    item['link'],
                    item['pic'],
                    item['star'],
                    item['rate'],
                    item['quote']
                )
            )
            self.conn.commit()
        except MySQLdb.Error, e:
            print 'Error %d %s' % (e.args[0], e.args[1])
 
        return item
