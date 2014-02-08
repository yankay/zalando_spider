# Scrapy settings for zalando_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zalando_spider'

SPIDER_MODULES = ['zalando_spider.spiders']
NEWSPIDER_MODULE = 'zalando_spider.spiders'

HTTPCACHE_ENABLED=True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zalando_spider (+http://www.yourdomain.com)'

CONCURRENT_REQUESTS = 128
CONCURRENT_REQUESTS_PER_DOMAIN = 128
CONCURRENT_ITEMS = 200

START_URLS = [
  "http://www.zalando.co.uk/esprit-online-shop/",
  "http://www.zalando.co.uk/marc-o-polo/"
  "http://www.zalando.co.uk/tom-tailor-online-shop/",
  "http://www.zalando.co.uk/s-oliver-online-shop/",
  "http://www.zalando.co.uk/benetton/"
]
