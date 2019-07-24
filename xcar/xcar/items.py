# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XcarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Bbs_Item(scrapy.Item):

    # 品牌论坛链接
    brand_url = scrapy.Field()
    # 车型链接
    series_url = scrapy.Field()
    # 论坛名称
    bbs_name = scrapy.Field()

    # 论坛链接
    name_url = scrapy.Field()

    # 车型ID
    series_id = scrapy.Field()
    # 车型
    series = scrapy.Field()
    # 品牌
    brand = scrapy.Field()
    # 模块
    module = scrapy.Field()
    # 模块地址
    module_url = scrapy.Field()

    # 主题数
    lasttopicnum = scrapy.Field()
    # 帖子总数
    lastbbsnum = scrapy.Field()

    # 精华数
    jh_count = scrapy.Field()
    # 全站认证车主
    rzcz_count = scrapy.Field()

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

    # 楼主等级
    grade = scrapy.Field()

    #名字
    name =scrapy.Field()

    # 地区
    district = scrapy.Field()

    # 车型
    model = scrapy.Field()

    # 帖子数量
    user_lastbbsnum = scrapy.Field()

    # 注册时间
    registration_time = scrapy.Field()

    # 帖子来源
    be_from = scrapy.Field()

    # 回帖时间
    time_postcont = scrapy.Field()

    # 点赞数
    of_use = scrapy.Field()

    # 内容
    content = scrapy.Field()

    # 精华数
    elite = scrapy.Field()

    # 车友会
    car_club = scrapy.Field()

    # 网站
    source = scrapy.Field()

    # 频道
    category = scrapy.Field()

    # 备注
    remark = scrapy.Field()
