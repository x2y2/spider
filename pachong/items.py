# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Movie250Item(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    pic = scrapy.Field()
    star = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()
