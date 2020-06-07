# -*- coding: utf-8 -*-
from pprint import pprint
from selenium.webdriver.chrome import webdriver

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentHrSpider(CrawlSpider):
    name = 'tencent_hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html?pcid=40001']

    browser = webdriver.ChromeRemoteConnection(remote_server_addr=locals())
    with browser.get("") as target:
        pass

    # 定义提取url地址规则 实例化规则
    rules = (
        # 提取list url
        Rule(LinkExtractor(
            restrict_xpaths=('//*[@class=\"correlation-degree\"]'
                             '//*[@class=\"recruit-list\"]'),
            tags=('a', 'area'), attrs=('href',)
        ), callback='parse_posts', follow=False),

        # 翻页 url
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    # def parse_item(self, response):
    #     item = {}
    #     #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
    #     #item['name'] = response.xpath('//div[@id="name"]').get()
    #     #item['description'] = response.xpath('//div[@id="description"]').get()
    #     return item

    def parse_posts(self, response):
        item = {}
        # self.logger.info('details_page: %s', response.url)
        item["link"] = response
        pprint('-' * 40)
        pprint(response)

        # yield scrapy.Request()

        return item

    def parse_details_page(self, response):
        pass
