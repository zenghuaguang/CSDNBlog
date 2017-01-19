#!/usr/bin/python
# -*- coding:utf-8 -*-

# from scrapy.contrib.spiders import  CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Rule, CrawlSpider

from CSDNBlog.items import CsdnblogItem


class CSDNBlogSpider(CrawlSpider):
    """爬虫CSDNBlogSpider"""

    name = "CSDNBlog"

    #减慢爬取速度 为1s
    download_delay = 1
    allowed_domains = ["blog.csdn.net"]
    start_urls = [

        #第一篇文章地址
        "http://blog.csdn.net/u012150179/article/details/11749017"
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow=('/u012150179/article/details'),
                              restrict_xpaths=('//li[@class="next_article"]')),
             callback='parse_item',
             follow=True)
    ]

    def parse_item(self, response):
        sel = Selector(response)

        #items = []
        #获得文章url和标题
        item = CsdnblogItem()

        article_url = str(response.url)
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        item['article_name'] = [n.encode('utf-8').strip() for n in article_name]
        item['article_url'] = article_url.encode('utf-8')
        return item
