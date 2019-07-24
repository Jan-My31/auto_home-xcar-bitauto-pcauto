# -*- coding: utf-8 -*-
import scrapy
from bitauto.items import Bbs_Item
# from scrapy_redis.spiders import RedisSpider
import copy, requests, json


class BitautoSpider(scrapy.Spider):
    name = 'bitauto_forum'
    allowed_domains = ['baa.bitauto.com']

    # start_urls=['http://baa.bitauto.com/foruminterrelated/brandforumlist_by_condition.html'] #全部论坛地址

    # 起始链接
    start_urls = [
        # 'http://baa.bitauto.com/benchisji/',
        # 'http://baa.bitauto.com/baoma7xichadianhundo/',
        # 'http://baa.bitauto.com/Panamera/',
        # 'http://baa.bitauto.com/aodia8/',
        # 'http://baa.bitauto.com/leikesasils/',
        # 'http://baa.bitauto.com/terracanhawtai/',
        # 'http://baa.bitauto.com/mashaladigt/',

        # 'http://baa.bitauto.com/baomax3/',
        # 'http://baa.bitauto.com/glc/',
        # 'http://baa.bitauto.com/aodiq5/',
        # 'http://baa.bitauto.com/xc60/',
        # 'http://baa.bitauto.com/leikesasirx/',
        # 'http://baa.bitauto.com/macan/',
        # 'http://baa.bitauto.com/leikesasinx/'
        'http://baa.bitauto.com/envision/',
        'http://baa.bitauto.com/aodia3/',
        'http://baa.bitauto.com/aodia6/',
        'http://baa.bitauto.com/highlander/',
        'http://baa.bitauto.com/kediyake/',
        'http://baa.bitauto.com/karoq/',
        'http://baa.bitauto.com/kamiq/',
        'http://baa.bitauto.com/equinox/',
        'http://baa.bitauto.com/tuguanl/',



    ]

    # 分布式
    # redis_key='bitauto:start_urls'
    # base_url='http://baa.bitauto.com'
    #

    # 遍历url————>请求页面
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # 论坛列表页
    def parse(self, response):
        try:
            # item = response.meta['item']
            # 论坛名称
            bbs_name = response.xpath(
                'string(//div[@class="bbs_name_style"]/div[@class="name_photo"]/h1)').extract_first().strip()
            # 主题数
            lasttopicnum = response.xpath(
                'string(//div[@class="bbs_name_style"]/div[@class="list_box"]/ul/li[1])').extract_first()
            # 帖子总数
            lastbbsnum = response.xpath(
                'string(//div[@class="bbs_name_style"]/div[@class="list_box"]/ul/li[2])').extract_first()
            table_list = response.xpath('//*[@id="divTopicList"]/div/ul')

            for table in table_list:

                # 标题
                posts = table.xpath('./li[@class="bt"]/a/span/text()').extract()
                if posts != []:
                    posts = posts[0].strip()

                # 标题链接
                posts_url = table.xpath('./li[@class="bt"]/a/@href').extract()
                if posts_url != []:
                    posts_url = posts_url[0].strip()

                # 回复值
                reply = table.xpath('./li[@class="hf"]/span/text()[1]').extract()
                if reply != []:
                    reply = reply[0].strip()

                # 浏览量
                viewcountid = table.xpath('./li[@class="hf"]/span/@viewcountid').extract()
                if viewcountid != []:
                    viewcountid = viewcountid[0]
                    view_count_Url = 'http://japi.yiche.com/japi/baa/topic/count/' + viewcountid + '?callback=Bitauto.Forum.Utils.setViewCount'
                    view_count_Url = response.urljoin(view_count_Url)
                    res = requests.get(view_count_Url)
                    page_view = \
                        json.loads(res.text.replace('/**/Bitauto.Forum.Utils.setViewCount(', '').replace(');', ''))[
                            'data'][
                            'totleCount']

                # 发帖人以及日期
                posted_name = table.xpath('./li[@class="zhhf"]/a/text()').extract()
                if posted_name != []:
                    posted_name = posted_name[0].strip()

                # 最后回帖人和日期
                finally_reply = table.xpath('./li[@class="zz"]/a/text()').extract()
                if finally_reply != []:
                    finally_reply = finally_reply[0].strip()
                reply_time = table.xpath('./li[@class="zz"]/span/text()').extract()
                if reply_time != []:
                    reply_time = reply_time[0].strip()

                posted_time = table.xpath('./li[@class="zhhf"]/span/text()').extract()
                if posted_time != []:
                    posted_time = posted_time[0].strip()
                    # if '2019' in posted_time or '2018' in posted_time:

                    if '2019' in posted_time or'2018' in posted_time or '2017' in posted_time :
                        posted_time = posted_time.replace('\r\n', '')

                        item = Bbs_Item()
                        item['bbs_name'] = bbs_name
                        item['lasttopicnum'] = lasttopicnum
                        item['posts'] = posts
                        item['lastbbsnum'] = lastbbsnum
                        item['posts_url'] = posts_url
                        item['reply'] = reply
                        item['page_view'] = page_view
                        item['posted_name'] = posted_name
                        item['posted_time'] = posted_time
                        item['finally_reply'] = finally_reply
                        item['reply_time'] = reply_time

                        yield scrapy.Request(url=posts_url, callback=self.detail_parse,
                                             meta={'item': copy.deepcopy(item)},
                                             dont_filter=True)

            # 获取下一页内容，用urljoin补全链接
            next_url = response.xpath('//*[@class ="next_on"]/@href').extract_first()
            if next_url is not None:
                next_url = response.urljoin(next_url)

                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
                print(next_url)

                print('接下来下一页是%s' % next_url)

            else:
                return None

        except Exception as ex:
            print(ex)

        # 具体帖子内容


    def detail_parse(self, response):
        try:
            item = response.meta['item']

            post_text_list = response.xpath('//div[@class="post_text post_text_sl"]')
            for post_text in post_text_list:
                # 帖子内容
                content = post_text.xpath(
                    'string(./div[@class="koubei_bbs_box"])').extract_first() + post_text.xpath(
                    'string(./div[@class="pingjia_box"])').extract_first() + post_text.xpath(
                    'string(./div[@class="post_width"])').extract_first() + post_text.xpath(
                    'string(./div[@class="post_koubei"])').extract_first() + post_text.xpath(
                    'string(./form[@id="voteForum"]//div[@class="diaoyan_list"])').extract_first() + post_text.xpath(
                    'string(//div[@class="koubei_jia"])').extract_first()
                content = content.replace('\n', '').replace(' ', '').replace('\xa0', '').replace(u'\u3000',
                                                                                                 '').replace('\r',
                                                                                                             '').replace(
                    '\t', '')

                item["content"] = content

                yield item


        except Exception as ex:
            print(ex)
