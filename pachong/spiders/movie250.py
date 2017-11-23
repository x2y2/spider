import scrapy
from scrapy.selector import Selector
from pachong.items import Movie250Item

class Movie250Spider(scrapy.Spider):
  name = "movie250"
  start_urls = ["https://movie.douban.com/top250/"]

  def parse(self,response):
    item = Movie250Item()
    selector = scrapy.Selector(response)
    Movie = selector.xpath('//div[@class="item"]')
    for info in Movie:
      rank =  info.xpath('div[@class="pic"]/em/text()').extract()[0]
      title = info.xpath('div[@class="pic"]/a/img/@alt').extract()[0]
      link = info.xpath('div[@class="pic"]/a/@href').extract()[0]
      pic = info.xpath('div[@class="pic"]/a/img/@src').extract()[0]
      star = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
      rate = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()[1]
      quote = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()[0]
      item['rank'] = rank.encode('utf-8')
      item['title'] = title.encode('utf-8')
      item['link'] = link.encode('utf-8')
      item['pic'] = pic.encode('utf-8')
      item['star'] = star.encode('utf-8')
      item['rate'] = rate.encode('utf-8')
      item['quote'] = quote.encode('utf-8')
      
      yield item
    next_page = response.xpath('//span[@class="next"]/a/@href')
    if next_page:
      url = response.urljoin(next_page[0].extract())
      yield scrapy.Request(url,self.parse)
