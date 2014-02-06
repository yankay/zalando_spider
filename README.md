zalando_spider
==============

Install
--------------

### Install Scrapy

[Install Guild](http://doc.scrapy.org/en/latest/intro/install.html)

In Ubuntu
```
sudo apt-get install python-pip build-essential libxml2-dev libxslt1-dev
sudo pip install Scrapy
```

### Clone Code

```
git clone https://github.com/yankay/zalando_spider.git
```

Run
--------------

```
cd <dir>
scrapy crawl zalando -o items.json -t json
```

Extends
--------------

There are 3 simple files needs to edit.

*   [Config File](https://github.com/yankay/zalando_spider/blob/master/zalando_spider/settings.py)
*   [Item Modle](https://github.com/yankay/zalando_spider/blob/master/zalando_spider/items.py)
*   [Script](https://github.com/yankay/zalando_spider/blob/master/zalando_spider/spiders/zalando_spider.py)

### Add new catatory

Add URL in START_URLS in  [Config File](https://github.com/yankay/zalando_spider/blob/master/zalando_spider/settings.py)

### Add new prop

* Add field in [Item Modle](https://github.com/yankay/zalando_spider/blob/master/zalando_spider/items.py)
* Add Script in [Script](https://github.com/yankay/zalando_spider/blob/master/zalando_spider/spiders/zalando_spider.py)

### Test Xpath

[Scrapy Shell](http://doc.scrapy.org/en/latest/topics/shell.html)
