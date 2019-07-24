# -*- coding: utf-8 -*-

import scrapy
from pcauto.items import Bbs_Item
import copy
from scrapy_splash import SplashRequest


class PcautoForumSpider(scrapy.Spider):
    name = 'pcauto_forum'
    allowed_domains = ['pcauto.com']

    # def parse(self, response):
    # pass

    start_urls = [


        'https://bbs.pcauto.com.cn/forum-20403.html',
        'https://bbs.pcauto.com.cn/forum-17369.html',
        'https://bbs.pcauto.com.cn/forum-14140.html',
        'https://bbs.pcauto.com.cn/forum-16876.html',
        'https://bbs.pcauto.com.cn/forum-24085.html',
        'https://bbs.pcauto.com.cn/forum-25645.html',
        'https://bbs.pcauto.com.cn/forum-27425.html',
        'https://bbs.pcauto.com.cn/forum-24715.html',
        'https://bbs.pcauto.com.cn/forum-16735.html',



    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):

        try:
            bbs_name = response.xpath('//div[@class="box-hd"]/span[@class="mark"]/text()').extract_first()

            title_list = response.xpath('//tbody/tr')
            for title in title_list:

                posts_url = title.xpath(
                    './th[@class="title checkbox_title2"]/span[@class="checkbox_title"]/a/@href').extract()
                if posts_url != []:
                    posts_url = response.urljoin(posts_url[0])
                posts = title.xpath(
                    './th[@class="title checkbox_title2"]/span[@class="checkbox_title"]/a/text()').extract()
                if posts != []:
                    posts = posts[0]

                # 回复数
                reply = title.xpath(
                    'normalize-space(./td[@class="nums"]/cite/text())').extract()
                if reply != []:
                    reply = reply[0]
                # # 浏览数
                # page_view = title.xpath('./td[@class="nums"]/em/text()').extract()
                # if page_view != []:
                #     page_view = page_view[0]

                # 发帖人姓名
                posted_name = title.xpath(
                    './td[@class="author"]/cite/a/text()').extract()
                if posted_name != []:
                    posted_name = posted_name[0]

                # # 回帖人姓名
                finally_reply = title.xpath(
                    './td[@class="lastpost"]/cite/a/text()').extract()
                if finally_reply != []:
                    finally_reply = finally_reply[0].replace('\n', '')
                # # 最后回复日期
                reply_time = title.xpath(
                    './td[@class="lastpost"]/em/text()').extract()
                if reply_time != []:
                    reply_time = reply_time[0]

                #  发帖日期
                posted_time = title.xpath(
                    './td[@class="author"]/em/text()').extract()
                if posted_time != []:
                    posted_time = posted_time[0]
                    if '19' == posted_time[:2] or '18' == posted_time[:2] or '17' == posted_time[:2]:
                        posted_time = posted_time.strip()

                        item = Bbs_Item()
                        item['bbs_name'] = bbs_name
                        item['posts_url'] = posts_url
                        item['posts'] = posts
                        item['posted_name'] = posted_name
                        item['posted_time'] = posted_time
                        item['reply'] = reply
                        # item['page_view'] = page_view
                        item['finally_reply'] = finally_reply
                        item['reply_time'] = reply_time
                        print(bbs_name,posts,posted_time)
                        yield scrapy.Request(posts_url, callback=self.detail_parse, meta={'item': copy.deepcopy(item)},
                                         dont_filter=True)
            next_page = response.xpath('//a[@class="next"]/@href').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                print(next_page)
                print('下一页是%s' % next_page)
                yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)
        except Exception as e:
            print(e)

    def detail_parse(self, response):
        try:


            # page_view =response.xpath('//span[@id="views"]/text()').extract_first()
            #
            # reply =response.xpath('//span[@class="yh"][2]/text()').extract_first()

            content = response.xpath(
                'normalize-space(//td[@id="first_post_msg_wrap"]/div[@class="post_msg replyBody"])').extract_first()
            content = content.replace('\xa0', '').replace('\u3000','')

            # page_view = response.xpath('//span[@id="views"]/text()').extract_first()
            #
            # reply = response.xpath('//span[@class="yh"][2]/text()').extract_first()
            # posts =response.xpath('//i[@id="subjectTitle"]/text()').extract_first()

            item = response.meta['item']

            # item =Bbs_Item()
            # item['page_view']=page_view
            # item['reply']=reply
            # item['posts']=posts
            item['content'] = content



            yield item
        except Exception as e:
            print(e)
