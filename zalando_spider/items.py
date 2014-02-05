# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PorductItem(Item):
    # define the fields for your item here like:
    req_url = Field()
    name = Field()
    brand = Field()
    category = Field()
    price = Field()
    old_price = Field()
    new_price = Field()
    color = Field()
    size = Field()