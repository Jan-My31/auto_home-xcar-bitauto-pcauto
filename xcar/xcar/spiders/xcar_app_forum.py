# -*- coding: utf-8 -*-
import scrapy


class XcarAppForumSpider(scrapy.Spider):
    name = 'xcar_app_forum'
    allowed_domains = ['xcar.com']
    start_urls = ['http://xcar.com/']

    def parse(self, response):
        pass
