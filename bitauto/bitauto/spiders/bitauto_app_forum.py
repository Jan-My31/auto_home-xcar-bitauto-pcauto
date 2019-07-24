# -*- coding: utf-8 -*-
import scrapy


class BitautoAppForumSpider(scrapy.Spider):
    name = 'bitauto_app_forum'
    allowed_domains = ['bba.bitauto.com']
    start_urls = ['http://bba.bitauto.com/']

    def parse(self, response):
        pass
