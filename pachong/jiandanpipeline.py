# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-
import os
import urllib

from pachong import settings

class JiandanPipeline(object):
  def process_item(self,item,spider):
    dir_path = os.path.join(settings.IMAGES_STORE,spider.name)
    if not os.path.exists(dir_path):
      os.makedirs(dir_path)
    for image_url in item['image_urls']:
      list_name = image_url.split('/')
      file_name = list_name[len(list_name) - 1]
      file_path = os.path.join(dir_path,file_name)
      print 'filepath: ',file_path
      if os.path.exists(file_path):
        continue
      with open(file_path,'wb') as fp:
        conn = urllib.urlopen(image_url)
        fp.write(conn.read())
    return item
