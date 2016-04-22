# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from scrapy.http import Request
import urlparse



class Website(Item): 
    pagetitle = Field() 
    description = Field()
    url = Field()
 
class DmozSpider(BaseSpider):
    name = "dmoz" # 
    allowed_domains = ["ko.wikipedia.org"] # 
    start_urls = [
        "https://ko.wikipedia.org/wiki/부산대"
    ] # start_urls 안에 들어있는 url이 parse 된다
 
    def parse(self, response):
        hxs = HtmlXPathSelector(response) 
        sites = hxs.select('//*[@id="mw-content-text"]//*/text()') 
        item = Website()
        item['pagetitle'] = ''.join(sites.extract()) 
        item['url'] = response.url
        yield item

        sites = hxs.select('//*[@id="mw-content-text"]//a/@href') 
        for site in sites:
            content = urlparse.urljoin(response.url, site.extract())
            yield Request(content, self.parse)

