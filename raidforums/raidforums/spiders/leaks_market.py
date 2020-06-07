# -*- coding: utf-8 -*-

from pprint import pprint

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector.unified import SelectorList

class LeaksMarketSpider(CrawlSpider):
    name = 'leaks_market'
    allowed_domains = ['raidforums.com']
    start_urls = ['https://raidforums.com/Forum-Leaks-Market']

    # 定义提取url地址规则 实例化规则
    rules = (
        # LinkExtractor ；链接提取器，提取url地址
        # callback 提取出来的url地址response会交给callback处理  详细页
        # follow 当前url地址响应是否重新经过 rules 来提取url地址  翻页提取
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        #
        # Rule(LinkExtractor(
        #     restrict_css=('.top-cat', '.sub-cat', '.cat-item')
        # ), callback='parse_directory', follow=True),

        Rule(LinkExtractor(
            restrict_xpaths=('//*[@id=\"forum-display\"]'
                             '//*[@class=\"forum-display__thread forum-display__thread--newfolder inline_row\"]'
                             '//*[@class=\" subject_new\"]'),
            tags=('a', 'area'), attrs=('href',)
        ), callback='parse_details_page', follow=False),
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