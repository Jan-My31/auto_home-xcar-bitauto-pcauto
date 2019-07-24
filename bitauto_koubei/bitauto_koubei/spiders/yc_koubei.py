# -*- coding: utf-8 -*-
import scrapy
import jsonpath,json,copy,re
from bitauto_koubei.items import BitautoKoubeiItem

class YcKoubeiSpider(scrapy.Spider):
    name = 'yc_koubei'
    allowed_domains = ['dianping.bitauto.com']
    start_urls = [
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A100%2C%22serialId%22%3A1660%2C%22pageSize%22%3A20%7D", # crv
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A4279%2C%22pageSize%22%3A20%7D",# xrv
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A2701%2C%22pageSize%22%3A20%7D",# rav4
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A2583%2C%22pageSize%22%3A20%7D",# 奇峻
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A2871%2C%22pageSize%22%3A20%7D", # 途观
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A2190%2C%22pageSize%22%3A20%7D", # 逍客
        #
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A5415%2C%22pageSize%22%3A20%7D",  # 探岳
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A3395%2C%22pageSize%22%3A20%7D",  # 奥迪q3
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A4711%2C%22pageSize%22%3A20%7D",  # CX-4
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A3736%2C%22pageSize%22%3A20%7D",  # 奥迪q2
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A5275%2C%22pageSize%22%3A20%7D",  # 途观
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A5398%2C%22pageSize%22%3A20%7D",# 途岳
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%225301%22%2C%22pageSize%22%3A20%7D",
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%224597%22%2C%22pageSize%22%3A20%7D",
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%222855%22%2C%22pageSize%22%3A20%7D",
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%224340%22%2C%22pageSize%22%3A20%7D",
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%222130%22%2C%22pageSize%22%3A20%7D",
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%223787%22%2C%22pageSize%22%3A20%7D",
        # "http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%224165%22%2C%22pageSize%22%3A20%7D",

        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%223379%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%223999%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%222573%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%222694%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%224742%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%225083%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%225352%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%224932%22%2C%22pageSize%22%3A20%7D',
        'http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22cTagId%22%3A%22%22%2C%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A2%2C%22serialId%22%3A%224936%22%2C%22pageSize%22%3A20%7D'
        ]


    '''
    param: {"tagId":"-10","currentPage":14,"serialId":3736,"pageSize":20}
    
    
    
    '''

    def start_requests(self):
        for url in self.start_urls:
            yield  scrapy.Request(url,callback=self.page_parse)

    def page_parse(self,response):
        data = json.loads(response.text)

        serialId=jsonpath.jsonpath(data,'$.data.carModel.csId')
        serialId=serialId[0]

        for page in range(1,100):#假设100页
            base_url ='http://dianping.bitauto.com/web_app/api/v1/review/get_review_list?param=%7B%22tagId%22%3A%22-10%22%2C%22currentPage%22%3A'+str(page)+'%2C%22serialId%22%3A'+str(serialId)+'%2C%22pageSize%22%3A20%7D'
            # print(base_url)
            yield scrapy.Request(url=base_url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        # try:
        data = json.loads(response.text)
        result = data["data"]

        data_list = result["list"]
        for info in data_list:

            item =BitautoKoubeiItem()
            item['posts_id']= info["id"]
            item['content']=info['content']
            item['series_name']=info['carName']
            if '2019' in info['createTime'] or '2018' in info['createTime'] or '2017' in info['createTime'] :
                item['release_date'] = info['createTime']

                # tagInfoList=info['tagInfoList']
                # if tagInfoList:
                #     tagInfoList=str(tagInfoList)
                #     discuss_merit =re.findall(r"#最满意(.*?)#最不满意",tagInfoList,re.S)
                #     discuss_defect=re.findall(r"#最不满意(.*?)}",tagInfoList,re.S)
                #     if discuss_merit is not None:
                #         discuss_merit=discuss_merit[0]
                #     if discuss_defect is not None:
                #         discuss_defect=discuss_defect[0]
                #         item['discuss_defect']=discuss_defect
                #         item['discuss_merit']=discuss_merit
                yield item
















