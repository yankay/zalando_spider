from __future__ import absolute_import

from scrapy.spider import Spider

from zalando_spider.items import PorductItem
from zalando_spider import settings

class DmozSpider(Spider):
    name = "zalando"


    allowed_domains = ["www.zalando.co.uk"]
    start_urls = settings.START_URLS
    

    def parse(self, response):
        item = PorductItem() 
	item['req_url'] = response.url
#        sel = Selector(response)
#sel.xpath("//div[@class='productInfos']/h1[@class='productName']/span[@itemprop='brand']/text()").extract()
#sel.xpath("//div[@class='productInfos']/h1[@class='productName']/span[@itemprop='name']/text()").extract()
        return item
