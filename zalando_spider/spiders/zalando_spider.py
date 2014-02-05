from __future__ import  absolute_import

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from zalando_spider.items import PorductItem
from zalando_spider import settings

class DmozSpider(Spider):
    name = "zalando"

    allowed_domains = ["www.zalando.co.uk"]
    start_urls = settings.START_URLS

    def page_type(self,response):
        sel = Selector(response)
        ilt_top_classes = sel.xpath("//div[@id='ilt_top']/@class").extract()
        for ilt_top_class in ilt_top_classes:
            for t in ilt_top_class.split(" "):
                if "PAGETYPE-CATALOG" in t:
                    yield t

    def is_category(self,response):
        for t in self.page_type(response):
            if "PAGETYPE-CATALOG_SEARCH" in t:
                return True

    def proc_category(self,response):
        def is_final_page(response):
            return True
        reqs = []
        if not is_final_page(response):
            pass
        sel = Selector(response)
        for item in sel.xpath("//a[@class='productBox']/@href").extract():
            url = item
            if not item.startswith("http"):
                url = "http://www.zalando.co.uk" + item
                reqs.append(Request(url, callback=self.parse))
        return reqs

    def is_item(self,response):
        for t in self.page_type(response):
            if "PAGETYPE-CATALOG_ARTICLE" in t:
                return True

    def proc_item(self,response):
        item = PorductItem() 
        item['req_url'] = response.url
        item['brand'] = sel.xpath("//div[@class='productInfos']/h1[@class='productName']/span[@itemprop='brand']/text()").extract()
        item['name'] = sel.xpath("//div[@class='productInfos']/h1[@class='productName']/span[@itemprop='name']/text()").extract()
        return item

    def parse(self, response):
        if self.is_category(response):
            return self.proc_category(response)
        if self.is_item(response):
            return self.proc_item()