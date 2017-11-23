import spynner
import pyquery
#import BeautifulSoup
from scrapy.http import HtmlResponse

class WebkitDownloaderTest(object):
  def process_request(self,request,spider):
    browser = spynner.Browser()
    #if 'Cookie' in request.headers.keys():
    #  browser.set_cookies(request.headers.Cookie)
    browser.create_webview()
    browser.set_html_parser(pyquery.PyQuery)
    browser.load(request.url,300)
    try:
      browser.wait_load(10)
    except:
      pass

    string = browser.html.encode('utf-8')
    renderedBody = str(string)
    browser.close()
    #return HtmlResponse(request.url,Cookies=browser.cookies,body=renderedBody)
    return HtmlResponse(request.url,body=renderedBody)

