from __future__ import  absolute_import

import string
from sets import Set

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from zalando_spider.items import PorductItem
from zalando_spider import settings

class DmozSpider(Spider):
    url_requested = Set()

    name = "zalando"
    basic_url = "http://www.zalando.co.uk/"

    allowed_domains = ["www.zalando.co.uk"]
    start_urls = settings.START_URLS

    def page_type(self,response):
        sel = Selector(response)
        ilt_top_classes = sel.xpath("//div[@id='ilt_top']/@class").extract()
        l = []
        for ilt_top_class in ilt_top_classes:
            for t in ilt_top_class.split(" "):
                if "PAGETYPE-CATALOG" in t:
                    l.append(t)
        return l

    def is_category(self,response):
        for t in self.page_type(response):
            if "PAGETYPE-CATALOG_SEARCH" in t:
                return True

    def proc_category(self,response):
        sel = Selector(response)
        for item in set(sel.xpath("//div[@class='pages']//a[.='>']/@href").extract()):
            url = item
            if not item.startswith("http"):
                url = basic_url + item
                if url not in url_requested:
                    url_requested.add(url)
                    yield Request(url, callback=self.parse)
        for item in sel.xpath("//a[@class='productBox']/@href").extract():
            url = item
            if not item.startswith("http"):
                url = basic_url + item
                if url not in url_requested:
                    url_requested.add(url)
                    yield Request(url, callback=self.parse)

    def is_item(self,response):
        for t in self.page_type(response):
            if "PAGETYPE-CATALOG_ARTICLE" in t:
                return True

    def proc_item(self,response):
        sel = Selector(response)
        item = PorductItem() 
        item['req_url'] = response.url
        item['brand'] = sel.xpath("//div[@class='productInfos']/h1[@class='productName']/span[@itemprop='brand']/text()").extract()
        item['name'] = sel.xpath("//div[@class='productInfos']/h1[@class='productName']/span[@itemprop='name']/text()").extract()
        item['category'] = sel.xpath("//div[@class='breadcrumbs']//ul//a//text()").extract()[3:]
        item['price'] = sel.xpath("//span[@itemprop='price']/text()").extract()
        item['old_price'] = sel.xpath("//span[@id='articleOldPrice']/text()").extract()
        item['new_price'] = sel.xpath("//span[@id='articlePrice']/text()").extract()
        if len(item['price']) == 0:
            item['price'] = item['new_price']
        item['color_available'] = sel.xpath("//ul[@class='colorList']//img/@title").extract()  
        item['size'] = map(string.strip,sel.xpath("//ul[@id='listProductSizes']/li/text()").extract())
        item['images'] = sel.xpath("//ul[@id='moreImagesList']//img/@src").extract()
        item['large_images'] =map( lambda s: s.replace('selector','large'), item['images'] )
        item['details'] =map(lambda s: " ".join(map(string.strip,s.xpath('.//text()').extract())), sel.xpath("//div[@id='productDetails']//ul//li"))

        for item in sel.xpath("//ul[@class='colorList']//a/@href").extract():
            url = basic_url + item
            if url not in url_requested:
                url_requested.add(url)
                yield Request(url, callback=self.parse)
                
        yield item

    def parse(self, response):
        if self.is_category(response):
            return self.proc_category(response)
        if self.is_item(response):
            return self.proc_item(response)
