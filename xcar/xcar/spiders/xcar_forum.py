# -*- coding: utf-8 -*-
import scrapy
from ..items import Bbs_Item
import copy


class XcarForumSpider(scrapy.Spider):
    name = 'xcar_forum'
    allowed_domains = ['xcar.com']
    start_urls = [

        # 'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=749',
        # 'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1486',
        # 'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=589',
        # 'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=825',
        # 'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1302',
        # 'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1078',
        # 'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1415'

        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1143',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=738',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=740',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=478',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1785',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=2010',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=2075',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1816',
        'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=545',
    ]

    # start_urls = ['http://www.xcar.com.cn/bbs/' ]
    # 初始页 爱卡汽车需要加上cookie才能访问页面
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse,
                                 cookies={'TY_SESSION_ID': '4d9b09a4-f858-4f93-b52d-049fba884563',
                                          '_fuv': '5586883955047', '_fwck_www': 'f95d013894a06550993218c371f0e56c',
                                          '_appuv_www': 'c97f19a4c6e75e17cd67e0886050f986',
                                          'Hm_lvt_53eb54d089f7b5dd4ae2927686b183e0': '1558082429,1558425141,1558425244,1558688398',
                                          '_Xdwuv': '5ce7b28ea09e8', '_Xdwnewuv': '1', '_PVXuv': '5c57b28fc6009',
                                          '_fwck_my': '83c62024b11e7c1125d9c1b568a86d70',
                                          '_appuv_my': '9d470273133836780dcbb5ba4aa48498',
                                          'fw_pvc': '1%3A1558923808%3B1%3A1558923826%3B1%3A1558924328%3B1%3A1558924447%3B1%3A1558924465',
                                          'fw_clc': '1%3A1558924447%3B1%3A1558924464%3B1%3A1558924469%3B1%3A1558924481%3B1%3A1558924493',
                                          'fw_slc': '1%3A1558923809%3B1%3A1558923826%3B1%3A1558924328%3B1%3A1558924448%3B1%3A1558924494',
                                          '_locationInfo_': '%7Burl%3A%22http%3A%2F%2Fjinan.xcar.com.cn%2F%22%2Ccity_id%3A%22225%22%2Cprovince_id%3A%2223%22%2Ccity_name%3A%22%25E6%25B5%258E%25E5%258D%2597%22%7D',
                                          'fw_exc': '1%3A1558923879%3B1%3A1558923880%3B1%3A1558924469%3B1%3A1558924489%3B1%3A1558924497',
                                          'place_prid_lin': '23', 'place_crid_lin': '225',
                                          'place_ip_lin': '111.14.97.12_1', 'isRemoveCookie': '1',
                                          'uv_firstv_refers': '', 'bbs_oldtopics': 'D29473435D21730272D',
                                          'bbs_visitedfid': '219D545D992D1958D464D1046',
                                          'Hm_lpvt_53eb54d089f7b5dd4ae2927686b183e0': '1558972682',
                                          '_Xdwstime': '1558972679'})

    def parse(self, response):

        bbs_name = response.xpath('//div[@class="forum-tit"]/h1/@title').extract_first()
        # item = response.meta['item']

        table_list = response.xpath('//div[@class="table-section"]/dl[@class="list_dl"]')
        for table in table_list:
            # 帖子名称
            posts = table.xpath('./dt/p[@class="thenomal"]/a/text()').extract()
            if posts != []:
                posts = posts[0]

            # 帖子链接
            posts_url = table.xpath('./dt/p[@class="thenomal"]/a/@href').extract()
            if posts_url != []:
                posts_url = posts_url[0]
                posts_url = response.urljoin(posts_url)

            # 回复数
            reply = table.xpath('./dd[@class="cli_dd"]/span[@class="fontblue"]/text()').extract()
            if reply != []:
                reply = reply[0]

            # 浏览数
            page_view = table.xpath('./dd[@class="cli_dd"]/span[@class="tcount"]/text()').extract()
            if page_view != []:
                page_view = page_view[0]

            # 发帖人姓名
            posted_name = table.xpath('./dd[@class="pub_dd"]/a/text()').extract()
            if posted_name != []:
                posted_name = posted_name[0]

            # 回帖人姓名
            finally_reply = table.xpath('./dd/a[@class="linkblack"]/text()').extract()
            if finally_reply != []:
                finally_reply = finally_reply[0]

            # 最后回复日期

            reply_time = table.xpath('./dd/span[@class="ttime"]/text()').extract()
            if reply_time != []:
                reply_time = reply_time[0]

            # print(posts,posts_url,reply,page_view,posted_name,posted_time,finally_reply,reply_time)

            # 发帖日期
            posted_time = table.xpath('./dd[@class="pub_dd"]/span/text()').extract_first()
            if '2019' in posted_time or '2018' in posted_time or '2017' in posted_time:
                posted_time = posted_time.replace('\r\n', '')
                item = Bbs_Item()
                item['bbs_name'] = bbs_name
                item['posts'] = posts
                item['posts_url'] = posts_url
                item['reply'] = reply
                item['page_view'] = page_view
                item['posted_name'] = posted_name
                item['posted_time'] = posted_time
                item['finally_reply'] = finally_reply
                item['reply_time'] = reply_time

                yield scrapy.Request(posts_url, callback=self.detail_parse, meta={'item': copy.deepcopy(item)},
                                     dont_filter=True)

        next_page = response.xpath(
            '//div[@class="table-article"]/div[@class="forumList_page"]/a[@class="page_down"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)

            print('接下来下一页是%s' % next_page)

            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)

    def detail_parse(self, response):

        try:

            item = response.meta['item']
            main_item_list = response.xpath('//div[@class="main item"][1]')
            for main_item in main_item_list:
                # 帖子内容
                content = main_item.xpath(
                    'string(./table//tr/td[@class="side_content"]/div[@class="mainwrap"]/div[@class="t_msgfont1"])').extract()
                if content != []:
                    content = content[0].replace(
                        '\n', '').replace(' ', '').replace('\xa0', '')

                    item['content'] = content

                    yield item

        except Exception as ex:
            print(ex)
