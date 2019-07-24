# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from twisted.enterprise import adbapi

class XcarPipeline(object):
    def process_item(self, item, spider):
        return item



class Xcar_MysqlPipeline(object):

    def __init__(self, host, user, password, db):
        params = dict(
            host=host,
            user=user,
            password=password,
            db=db,
            charset='utf8',  # 不能用utf-8
            cursorclass=pymysql.cursors.DictCursor
        )
        # 使用Twisted中的adbapi获取数据库连接池对象
        self.dbpool = adbapi.ConnectionPool('pymysql', **params)

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings文件中的配置
        host = crawler.settings.get('HOST')
        user = crawler.settings.get('USER')
        password = crawler.settings.get('PASSWORD')
        db = crawler.settings.get('DB')
        return cls(host, user, password, db)

    def process_item(self, item, spider):
        # 使用数据库连接池对象进行数据库操作,自动传递cursor对象到第一个参数
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 设置出错时的回调方法,自动传递出错消息对象failure到第一个参数
        query.addErrback(self.on_error, spider)
        return item

    def do_insert(self, cursor, item):


        sql = 'INSERT INTO xcar_list(bbs_name,posts,posts_url,reply,page_view,posted_name,posted_time,content)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        args = (

            item['bbs_name'],
            item['posts'],
            item['posts_url'],
            item['reply'],
            item['page_view'],
            item['posted_name'],
            item['posted_time'],
            # item['finally_reply'],
            # item['reply_time'],
            item['content'],


        )

        cursor.execute(sql, args)

    def on_error(self, failure, spider):
        spider.logger.error(failure)
