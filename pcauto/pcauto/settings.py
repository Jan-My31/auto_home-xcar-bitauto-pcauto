# -*- coding: utf-8 -*-

# Scrapy settings for pcauto project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pcauto'

SPIDER_MODULES = ['pcauto.spiders']
NEWSPIDER_MODULE = 'pcauto.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'pcauto (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',

# 'User-Agent': 'Android	4.4.4	autohome.spiders	9.11.0	Android',
#     'Accept-Encoding': 'gzip',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'pcauto.middlewares.PcautoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#
# }
# 添加splash服务地址
SPLASH_URL = 'http://127.0.0.1:8050/'

DOWNLOADER_MIDDLEWARES = {

    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'pcauto.middlewares.PcautoDownloaderMiddleware': 543,
    'pcauto.middlewares.RandomUserAgentMiddlware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 'pcauto.middlewares.RandomProxyMiddleware':543,
    # 'scrapy.downloadermiddlewares.HttpProxyMiddleware': None
}

# 设置自定义DUPEFILTER_CLASS去重的类DUPEFILTER_CLASS
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Cache存储HTTPCACHE_STORAGE
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


SPLASH_COOKIES_DEBUG = True
# 随机usergent
RANDOM_UA_TYPE = 'random'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'pcauto.pipelines.PcautoPipeline': 300,
    'pcauto.pipelines.Pcauto_MysqlPipeline': 200
}


# SPIDER_MIDDLEWARES = {
#     'scrapy_deltafetch.DeltaFetch': 100,
# }
#
# DELTAFETCH_ENABLED = True
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# Mysql数据库参数
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = '121314'
DB = 'car_data'

# 日志存储
EED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'DEBUG'
# LOG_LEVEL= 'ERROR'

# LOG_FILE = "spider.log"


# 出现状态码之再次访问
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408]
RETRY_TIMES = 100

HTTPERROR_ALLOWED_CODES = [403]
