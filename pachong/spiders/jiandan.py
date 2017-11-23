#coding:utf-8
import scrapy
from pachong.jiandanitems import JiandanItem

from scrapy.crawler import CrawlerProcess

class JiandanSpider(scrapy.Spider):
  name = "jiandan"
  start_urls = ["http://jiandan.net/ooxx"]

  def parse(self,response):
    item = JiandanItem()
    image_urls = response.xpath('//p/img/@src').extract()
    item['image_urls'] = image_urls
    yield item
    next_url = response.xpath('//a[@class="previous-comment-page"]/@href').extract()
    if next_url:
      url = response.urljoin(next_url[0].encode('utf-8'))
      print 'next page: ',url
      yield scrapy.Request(url,callback=self.parse)
