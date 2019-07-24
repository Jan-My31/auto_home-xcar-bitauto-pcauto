# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutohomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Autohome_koubeiItem(scrapy.Item):

    series_id =scrapy.Field() #--车型ID
    brand=scrapy.Field()#--车型ID
    series=scrapy.Field()#--车型ID
    title=scrapy.Field()#--标题 全部在售/2018款
    guide_price=scrapy.Field()#--官方指导价
    grade=scrapy.Field()#--综合评分
    impression_merit=scrapy.Field()#--网友印象 优点
    impression_defect=scrapy.Field()#	--缺点
    oil_wear_1=scrapy.Field()#--油耗
    oil_wear_2=scrapy.Field()#--油耗
    oil_wear_3=scrapy.Field()#--油耗
    oil_wear_4=scrapy.Field()#--油耗
    quality_research=scrapy.Field()#--质量研究
    failure_ratio=scrapy.Field()#--故障比例
    comparative_quality_ranking=scrapy.Field()#--对比质量排行
    quantity=scrapy.Field()#--质量评价人数
    source=scrapy.Field()#--网站
    category=scrapy.Field()#--频道

class Autohome_clubItem(scrapy.Item):
    bbs_id=scrapy.Field()
    bbs_name = scrapy.Field()
    # 模块
    module= scrapy.Field()
    # 模块地址
    module_url = scrapy.Field()
    # 帖子名
    posts = scrapy.Field()
    # 标题链接
    posts_url = scrapy.Field()
    # 帖子id
    posts_id = scrapy.Field()
    # 回复数
    reply = scrapy.Field()
    # 浏览数
    page_view = scrapy.Field()
    # 发帖人姓名
    posted_name = scrapy.Field()
    # 发帖日期
    posted_time = scrapy.Field()
    # 回帖人姓名
    finally_reply = scrapy.Field()
    # 最后回复日期
    reply_time = scrapy.Field()
    # 姓名
    name = scrapy.Field()

    #用户id
    userid =scrapy.Field()


    topicinfo=scrapy.Field()

    postuserid=scrapy.Field()

    postusername=scrapy.Field()

    authseries=scrapy.Field()
    # 等级
    grade = scrapy.Field()
    # 用户帖子数
    user_lastbbsnum = scrapy.Field()
    # 地区
    district = scrapy.Field()

    # 车型
    model = scrapy.Field()

    # 注册时间
    registration_time = scrapy.Field()

    # 点赞数
    of_use = scrapy.Field()

    # --内容
    content = scrapy.Field()

    # 帖子地址
    posts_url = scrapy.Field()

    name_id =scrapy.Field()

    # 精华数
    elite = scrapy.Field()

    # --车友会
    car_club = scrapy.Field()

    # 网站
    source = scrapy.Field()

    # --频道
    category = scrapy.Field()

    # --备注
    remark = scrapy.Field()
