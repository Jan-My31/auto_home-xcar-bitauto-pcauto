# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2


class BitautoKoubeiPipeline(object):

    def __init__(self, kargs):
        self.conn = psycopg2.connect(database=kargs["pg_dbname"], user=kargs["pg_user"], password=kargs["pg_password"],
                                     host=kargs["pg_host"], port=kargs["pg_port"])
        self.cursor = self.conn.cursor()
        self.bitauto_sql = """INSERT INTO bitauto_koubei(
                      
                       posts_id,
                       content,
                       series_name,
                       release_date
                      
                  
                    
                        )
                        VALUES
                        ( %s, %s, %s,%s)"""

    @classmethod
    def from_crawler(cls, crawler):
        pg_param = dict(
            pg_host=crawler.settings.get("PG_HOST"),
            pg_port=crawler.settings.get("PG_PORT"),
            pg_user=crawler.settings.get("PG_USER"),
            pg_password=crawler.settings.get("PG_PASSWORD"),
            pg_dbname=crawler.settings.get("PG_DBNAME"),
        )
        return cls(pg_param)

    def process_item(self, item, spider):
        # self.cursor.execute(self.koubei_sql, (item["user_id"], item["series_id"], item["series_name"], item["release_date"], item["discuss_title"], item["discuss_merit"], item["discuss_defect"], item["discuss_facade"], item["discuss_trim"], item["discuss_space"], item["discuss_price"], item["discuss_impetus"], item["discuss_control"], item["discuss_oil_wear"], item["discuss_comfort"], item["discuss_why_choice"],item["page_view"],item["reply"],item["update_date"]))
        self.cursor.execute(self.bitauto_sql,
                            (item['posts_id'], item['content'], item['series_name'], item['release_date']
                             # item['discuss_defect'],item['discuss_merit']

                             ))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
