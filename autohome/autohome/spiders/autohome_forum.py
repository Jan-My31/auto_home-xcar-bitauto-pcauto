# -*- coding: utf-8 -*-
import scrapy
import jsonpath, json, copy, re
from autohome.items import Autohome_clubItem


class AutohomeForumSpider(scrapy.Spider):
    name = 'autohome_forum'
    #
    start_urls = [

        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=4453&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=4690&bt=c&r=0&ss=0&o=0&p=20&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=4217&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=3554&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=771&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=4235&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=3170&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=18&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0',
        'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=4274&bt=c&r=0&ss=0&o=0&p=100&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0'

        #

        # 'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=4658&bt=c&r=0&ss=0&o=0&p=230&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.page_parse)

    def page_parse(self, response):
        data = json.loads(response.text)
        pagecount = jsonpath.jsonpath(data, '$.result.pagecount')
        bbs_id = jsonpath.jsonpath(data, '$.result.clubid')

        pagecount = pagecount[0]
        bbs_id = bbs_id[0]
        print(bbs_id, pagecount)

        for page in range(1, int(pagecount + 1)):


            # 'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=4658&bt=c&r=0&ss=0&o=0&p=2&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0'
            base_url = 'https://club.app.autohome.com.cn/club_v9.6.0/club/topicslist?pm=2&b=' + str(
                bbs_id) +'&bt=c&r=0&ss=0&o=0'+ '&p=' + str(page) + '&s=50&qf=0&c=370100&t=0&v=9.11.0&d=f976449d_0a5d_4508_a5ec_78f5cbf8eccc&n=0'

            yield scrapy.Request(base_url, callback=self.parse, dont_filter=True)
            # print(base_url)

    def parse(self, response):
        data = json.loads(response.text)
        result = data["result"]
        data_list = result["list"]
        for info in data_list:
            posts_id = info["topicid"]

            item = Autohome_clubItem()

            item['bbs_name'] = info["bbsname"]
            item['posts'] = info["title"]

            item['posts_id'] = info["topicid"]

            # 回复数
            item['reply'] = info["replycounts"]

            # 发帖人姓名
            item['posted_name'] = info["postusername"]

            # 最后回复日期
            item['reply_time'] = info["lastreplydateo"]
            # 类型
            item['module'] = info["topictype"]

            item['name_id'] = info["userid"]

            item['name'] = info["username"]

            # # item['topicinfo'] =info["topicinfo"]
            item['model'] = info["authseries"]

            if '2019' in info["posttopicdateo"] or '2018' in info["posttopicdateo"] or '2017' in info["posttopicdateo"] :
                item['posted_time'] = info["posttopicdateo"]

                posts_url = ' http://forum.app.autohome.com.cn/forum_v9.8.0/forum/club/topiccontent-a2-pm2-t' + str(
                posts_id) + '-o0-p1-s20-c1-nt0-fs0-sp1-al0-cw0-i0-ct0-mid0-abB-isar0.json'
                posts_url = posts_url.replace(' ', '')
                item['posts_url']=posts_url

                yield scrapy.Request(url=posts_url, callback=self.detail_parse, dont_filter=True,
                                 meta={'item': copy.deepcopy(item)})

    def detail_parse(self, response):
        item = response.meta['item']
        page_view = response.xpath('//span[@class="view"]/text()').extract()
        if page_view !=[]:
            page_view=page_view[0]
            page_view = page_view.strip('浏览')
        content = response.xpath('string(//div[@class="host-content"]/div[1])').extract()
        if  content !=[]:
            content=content[0].replace('\n','').replace(' ','').replace('\xa0','')
            content=re.sub(re.compile(r"function(.*?)document"),"",content)



            item['page_view'] = page_view
            item['content'] = content


            yield item

