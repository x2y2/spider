#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from pachong.jditems import JdItem
from scrapy.crawler import CrawlerProcess

class JiandanSpider(scrapy.Spider):
  name = "jd"
  start_urls = ["https://list.jd.com/list.html?cat=9987,653,655"]

  def parse(self,response):
    name = []
    shop = []
    commit = []
    item = JdItem()
    price = response.xpath('//div[@class="p-price"]/strong[@class="J_price"]/i/text()').extract()
    names = response.xpath("//div[contains(@class,'p-name')]/a/em/text()").extract()
    name = [n.strip().encode('ISO 8859-1') for n in names if names]
    commits = response.xpath('//div[@class="p-commit"]/strong/a[@class="comment"]/text()').extract()
    commit = [c.strip().encode('ISO 8859-1') for c in commits if commits]
    shops = response.xpath('//div[@class="p-shop"]/span/a/text()').extract()
    shop = [s.strip().encode('ISO 8859-1') for s in shops if shops]
    item['name'] = name
    item['price'] = price
    item['commit'] = commit
    item['shop'] = shop
    yield item
    
    next_url = response.xpath('//a[@class="pn-next"]/@href').extract()
    if next_url:
      url = response.urljoin(next_url[0].encode('utf-8'))
      print 'next page: ',url
      yield scrapy.Request(url,callback=self.parse)
